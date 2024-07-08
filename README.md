# FAT template

<p align="center">
    <a href="https://github.com/matapatos/fat-template/actions"><img alt="GitHub Actions Workflow Status (main)" src="https://img.shields.io/github/actions/workflow/status/matapatos/fat-template/tests.yml"></a>
    <a href="https://codecov.io/gh/matapatos/fat-template" ><img alt="Code Coverage" src="https://img.shields.io/codecov/c/github/matapatos/fat-template/main"></a>
    <a href="https://packagist.org/packages/matapatos/wp-fastendpoints"><img alt="Supported Python Version" src="https://img.shields.io/badge/3.10 | 3.11 | 3.12-versions?label=python&color=blue"></a>
    <a href="https://opensource.org/licenses/MIT"><img alt="Software License" src="https://img.shields.io/badge/MIT-license?label=license"></a>
</p>

**FAT template** is a lightweight Full-Stack template with out of the box support for FastAPI + AlpineJS + TailwindCSS.

## Features

- Hot reloading dev server - no need to refresh the browser for viewing changes
- JavaScript and TypeScript support
- [FastAPI](https://fastapi.tiangolo.com/)
- [AlpineJS](https://alpinejs.dev/)
- [TailwindCSS](https://tailwindcss.com/)

## Requirements

- Python ^3.10
- FastAPI
- AlpineJS
- TailwindCSS

## Development

### Installation

```bash
make install
```

### Backend server

```bash
make dev:backend
```

### Frontend server

```bash
make dev:frontend
```

## Production

### Installation

```bash
make install:prod
```

### Server

```bash
make prod
```

## Lint

```bash
make lint
```

## Tests

```bash
make test
```

### Unit tests

```bash
make test:unit
```

### Integration tests

```bash
make test:integration
```

### End-to-end tests

```bash
make test:e2e
```

## Format

```bash
make format
```

FAT template was created by **[André Gil](https://www.linkedin.com/in/andre-gil/)** and is open-sourced software licensed under the **[MIT license](https://opensource.org/licenses/MIT)**.

