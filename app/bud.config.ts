import type {Bud} from '@roots/bud';

/**
 * bud.js configuration
 */
export default async (bud: Bud) => {
  bud
    /**
     * App entrypoints
     */
    .entry('app', ['@js/index.js', '@css/index.css']).html()
    /**
     * Sets the JS/CSS resources to those
     */
    .setPath('@src', 'resources')
    /**
     * Watch for file changes in views directory
     */
    .watch(['views'])
    /**
     * Where static files resides
     */
    .assets('static')
    /**
     * Aliases to use within the app
     */
    .alias('@css', bud.path('@src/css'))
    .alias('@js', bud.path('@src/js'))
    .alias('@static', bud.path('@src/static'))
    /**
     * Optimize for production
     */
    .when(bud.isProduction, bud.minimize)
    .when(bud.isProduction, bud.splitChunks)
};
