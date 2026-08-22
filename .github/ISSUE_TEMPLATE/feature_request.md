name: Feature Request
description: Suggest a new feature for the integration
title: "[FEATURE] "
labels: ["enhancement"]

body:
  - type: markdown
    attributes:
      value: |
        Thank you for suggesting a feature! Help us understand your idea.

  - type: textarea
    id: description
    attributes:
      label: Description
      description: Clear description of the feature
    validations:
      required: true

  - type: textarea
    id: usecase
    attributes:
      label: Use Case
      description: Why would this feature be useful?
    validations:
      required: true

  - type: textarea
    id: alternatives
    attributes:
      label: Alternatives Considered
      description: Any alternative approaches you've thought of?

  - type: textarea
    id: additional
    attributes:
      label: Additional Context
      description: Any other relevant information?
