name: Bug Report
description: Report a bug in the LD2410D-B integration
title: "[BUG] "
labels: ["bug"]

body:
  - type: markdown
    attributes:
      value: |
        Thank you for reporting a bug! Please provide as much detail as possible.

  - type: input
    id: ha_version
    attributes:
      label: Home Assistant Version
      placeholder: "2024.1.0"
    validations:
      required: true

  - type: input
    id: device_model
    attributes:
      label: Sensor Model
      placeholder: "HLK-LD2410B or HLK-2410D-B"
    validations:
      required: true

  - type: textarea
    id: description
    attributes:
      label: Description
      description: Clear description of the bug
    validations:
      required: true

  - type: textarea
    id: steps
    attributes:
      label: Steps to Reproduce
      placeholder: |
        1. 
        2. 
        3.
    validations:
      required: true

  - type: textarea
    id: expected
    attributes:
      label: Expected Behavior
    validations:
      required: true

  - type: textarea
    id: actual
    attributes:
      label: Actual Behavior
    validations:
      required: true

  - type: textarea
    id: logs
    attributes:
      label: Relevant Logs
      render: shell
      description: |
        Check Home Assistant logs at Settings → System → Logs
        Look for "ld2410" or related errors

  - type: textarea
    id: additional
    attributes:
      label: Additional Context