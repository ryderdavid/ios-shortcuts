# Calendar-Copy

Syncs events from a source calendar to a destination calendar.

## Logic
- **Window:** 3-day look-ahead.
- **Deduplication:** Uses a tag `[SYNCED]` in the event notes to identify previously synced events.
- **Filters:** Only copies events without any attendees (invitees).

## Setup
1. Edit `calendar-copy.cherri` to set your source and destination calendars.
2. Build the shortcut using: `cherri calendar-copy.cherri -o dist/calendar-copy.shortcut`
3. Import the `.shortcut` file on your iOS device.

## Building
The shortcut is written in [Cherri](https://cherrilang.org/), a programming language that compiles to iOS Shortcuts.

```bash
# Install Cherri (macOS)
brew tap electrikmilk/cherri
brew install electrikmilk/cherri/cherri

# Build the shortcut
cherri calendar-copy.cherri -o dist/calendar-copy.shortcut
```

## Status
Currently a prototype that demonstrates:
- Date arithmetic (calculating 3-day window)
- Date formatting
- Alert and result display

TODO: Implement the actual event filtering and copying logic.
