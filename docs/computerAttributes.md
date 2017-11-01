# Computer Attributes
##### A list of all of the attributes in the ../data/computerAttributes.csv and their meanings:
- **dbID (int)**: This is the unique ID primary key of the computer in the availability database. Included for reference.

- **computerName (string)**: This is the name of the computer as it exists in Active Directory

- **requiresLogon (boolean as int)**: This is to allow for future functionality, as machines that do not require a logon are not currently tracked by this application. _These machines should be excluded from reporting._

- **isDesktop (boolean as int)**: 1 = desktop, 0 = laptop

- **inJackson (boolean as int)**: 1 = in Jackson Library, 0 = in Music Library

(The following items are likely null for laptops)
- **location (string)**: A descriptor of the location of the machine

- **is245 (boolean as int)**: 1 = Available during the 24/5 hours, 0 = Only available during normal hours.

- **floor (int)**: 1 = first floor, 2 = second floor, etc.

- **numMonitors (int)**: 1 or 2 monitors. Could be boolean, but there may be three monitor machines counted.

- **largeMonitor (boolean as int)**: 1 = monitor(s) > 22" in size, 0 = monitor(s) <= 22" in size.

- **adjacentWindow (boolean as int)**: 1 = computer is directly adjacent to a window, no other local machines are closer to this window. 0 = not adjacent to window

- **collaborativeSpace (boolean as int)**: 1 = space is intended for group study (3+ students), 0 = intended for 2 or fewer users

- **roomIsolated (boolean as int)**: 1 = computer is only machine in room with door. 0 = computer is in an open area.

- **inQuietArea (boolean as int)**: 1 = computer is on a quiet floor. 0 = computer is on non-quiet or group study floor.
