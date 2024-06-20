import Alpine from 'alpinejs';

window.Alpine = Alpine;

Alpine.start();

/**
 * Hot reload (can be removed by React and Vue users)
 */
if (import.meta.webpackHot) {
  import.meta.webpackHot.accept(console.error);
}
