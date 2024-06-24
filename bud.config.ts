import type {Bud} from '@roots/bud';

/**
 * bud.js configuration
 */
export default async (bud: Bud) => {
  bud
    /**
     * App entrypoints
     */
    .entry({
      app: ['@scripts/app.js', '@styles/app.css'],
    })
    /**
     * Sets the JS/CSS resources to those
     */
    .setPath('@src', 'app/resources')
    .setPath('@dist', 'app/dist')
    /**
     * Watch for file changes in views directory
     */
    .watch(['app/resources/views'])
    /**
     * Where static files resides
     */
    .assets('@static')
    /**
     * Aliases to use within the app
     */
    .alias('@styles', bud.path('@src/css'))
    .alias('@scripts', bud.path('@src/js'))
    .alias('@static', bud.path('@src/static'))
    /**
     * Optimize for production
     */
    .minimize()
    .splitChunks()
    /**
     * Development server
     */
    .proxy('http://127.0.0.1:8000')
    .serve('http://0.0.0.0:3000')
};
