# Calendar-Copy

Syncs events from a source calendar to a destination calendar.

## Logic
- **Window:** 3-day look-ahead.
- **Deduplication:** Uses a tag `sync-id` in the event notes/description to identify previously synced events.
- **Filters:** Only copies events without any invitees.

## Setup
1. Define your source and destination calendars in the YAML.
2. Build the shortcut using the `shortcut-builder`.
3. Import the `.shortcut` file on your iOS device.
