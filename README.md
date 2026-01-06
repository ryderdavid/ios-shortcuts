# iOS Shortcuts

A monorepo for managing and building iOS Shortcuts using YAML.

## Structure
- `packages/`: Shortcut definitions and compiled files.
- `tools/`: Development tools.
- `docs/`: Documentation.

## Duplicate Prevention Logic
The shortcuts in this repository (like `calendar-copy`) use a tag-based deduplication strategy. 
When an event is copied, a unique identifier (tag) is added to the event's notes or description. 
Before copying an event, the shortcut checks if an event with the same tag already exists in the destination calendar to prevent duplicates.
