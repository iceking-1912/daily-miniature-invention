/**
 * AtmosphericStateEngine: A middleware-driven state management pattern
 * Exploring asynchronous interceptors and immutable state transitions.
 */

type Middleware<T> = (state: T, next: (state: T) => Promise<T>) => Promise<T>;

export class AtmosphericStateEngine<T extends object> {
  private state: T;
  private middleware: Middleware<T>[] = [];

  constructor(initialState: T) {
    this.state = Object.freeze({ ...initialState });
  }

  /**
   * Registers a middleware function to intercept state updates.
   */
  public use(fn: Middleware<T>): void {
    this.middleware.push(fn);
  }

  /**
   * Dispatches an update request through the middleware chain.
   */
  public async dispatch(patch: Partial<T>): Promise<T> {
    const finalUpdate = async (currentState: T): Promise<T> => {
      return Object.freeze({ ...currentState, ...patch });
    };

    const runner = (index: number): (s: T) => Promise<T> => {
      if (index === this.middleware.length) {
        return finalUpdate;
      }
      return (currentState: T) => this.middleware[index](currentState, runner(index + 1));
    };

    this.state = await runner(0)(this.state);
    return this.state;
  }

  /**
   * Returns the current immutable state.
   */
  public getState(): T {
    return this.state;
  }
}

// Example Usage Simulation
(async () => {
  const engine = new AtmosphericStateEngine({ pressure: 1013, status: 'stable' });

  // Middleware: Logging
  engine.use(async (state, next) => {
    console.log('[LOG] Current State:', state);
    const result = await next(state);
    console.log('[LOG] Next State:', result);
    return result;
  });

  // Middleware: Safety Valve (Environmental constraint)
  engine.use(async (state, next) => {
    const updated = await next(state);
    if (updated.pressure > 1100) {
      return { ...updated, status: 'critical_venting' };
    }
    return updated;
  });

  await engine.dispatch({ pressure: 1150 });
})();