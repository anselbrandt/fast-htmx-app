# FastAPI / htmx

### Install

Install the appropriate Tailwind CLI binary (see below)

```
uv sync
```

### Run

```
task dev

or

uv run uvicorn main:app --reload --reload-include '**/*.html' --reload-include '**/*.css'
```

### Tests

```
task test

or

uv run pytest
```

### Build CSS

```
task buildcss

or

./tailwindcss -o static/tailwind.css
```

### Tailwind

This project uses the [ Tailwind standalone CLI](https://tailwindcss.com/blog/standalone-cli)

You must [download](https://github.com/tailwindlabs/tailwindcss/releases/latest) the build for your OS/arch.

```
# Example for macOS arm64
curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-macos-arm64
chmod +x tailwindcss-macos-arm64
mv tailwindcss-macos-arm64 tailwindcss
```

Below commands are for reference. Tailwind CLI is run automatically by FastAPI.

```
# Create a tailwind.config.js file
./tailwindcss init

# Start a watcher
./tailwindcss -i input.css -o output.css --watch

# Compile and minify your CSS for production
./tailwindcss -i input.css -o output.css --minify
```
