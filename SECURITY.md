# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.0   | ✅ Yes             |
| < 1.0.0 | ❌ No              |

## Reporting a Vulnerability

**Please do not publicly disclose security vulnerabilities.**

If you discover a security vulnerability, please email the maintainer directly instead of using the issue tracker.

Include in your report:
- Description of the vulnerability
- Potential impact
- Affected versions
- Suggested fix (if available)

## Security Best Practices

When using this integration:

1. **Keep Home Assistant Updated**: Regularly update Home Assistant to get security patches
2. **Bluetooth Security**: Ensure your Bluetooth adapter is secured and up-to-date
3. **Network Security**: Use firewall rules to restrict access to Home Assistant
4. **Local Communication**: This integration operates on local Bluetooth only (not cloud-based)
5. **Dependencies**: Monitor dependencies for security updates

## Dependencies Security

This integration relies on:
- `ld2410-ble` - Community-maintained Bluetooth library
- `bluetooth-data-tools` - Home Assistant Bluetooth utilities
- `bluetooth_adapters` - Home Assistant Bluetooth component

Keep these packages updated through Home Assistant updates.

## Acknowledgments

We appreciate researchers and users who responsibly report security issues.