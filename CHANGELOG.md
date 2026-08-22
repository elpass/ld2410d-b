# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-08-22

### Added
- Initial release of LD2410D-B integration for Home Assistant
- Support for HLK-LD2410B model
- Support for HLK-2410D-B model (new)
- Automatic Bluetooth device discovery
- Binary sensors for motion and occupancy detection
- Comprehensive sensor suite for distance and energy measurements
- 9-gate motion and static energy detection
- Real-time data updates via coordinator pattern
- Configuration flow UI
- Localization support (strings.json)

### Features
- Motion detection with MOTION device class
- Occupancy detection with OCCUPANCY device class
- Distance measurements in centimeters
- Energy level readings for diagnostic purposes
- Automatic connection management
- Graceful error handling and status reporting

## [Unreleased]

### Planned
- Support for additional LD2410 variants
- Configuration options for sensitivity tuning
- Historical data tracking
- Performance optimizations