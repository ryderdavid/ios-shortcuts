# iOS Shortcuts

A monorepo for managing and building iOS Shortcuts using [Cherri](https://cherrilang.org/).

## Structure
- `packages/`: Shortcut definitions and compiled files.
- `docs/`: Documentation.

## Building Shortcuts

This project uses Cherri, a programming language that compiles directly to signed iOS Shortcuts.

### Install Cherri

```bash
# macOS
brew tap electrikmilk/cherri
brew install electrikmilk/cherri/cherri
```

### Build a Shortcut

```bash
# Navigate to a package
cd packages/calendar-copy

# Compile to a signed shortcut
cherri calendar-copy.cherri -o dist/calendar-copy.shortcut
```

## Duplicate Prevention Logic

The shortcuts in this repository (like `calendar-copy`) use a tag-based deduplication strategy. 
When an event is copied, a unique identifier tag is added to the event's notes. 
Before copying an event, the shortcut checks if an event with the same tag already exists in the destination calendar to prevent duplicates.
