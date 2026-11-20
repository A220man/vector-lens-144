"""Test that skill name uses hyphen, not colon (Issue #39 fix)."""

import re
import pathlib

SKILL_MD = pathlib.Path("/var/lib/alan-portfolio/workspaces/ryan/vector-lens-144/skills/react-components/SKILL.md")


def test_skill_name_uses_hyphen():
    """Skill name must contain only letters, numbers, hyphens, underscores, dots, and spaces."""
    content = SKILL_MD.read_text()
    # Extract the name line
    name_match = re.search(r'^name:\s*(.+)$', content, re.MULTILINE)
    assert name_match, "SKILL.md must contain a 'name:' line"
    skill_name = name_match.group(1).strip()
    # Must not contain colon
    assert ":" not in skill_name, f"Skill name must not contain colon, got: {skill_name!r}"
    # Must match valid skill name pattern
    assert re.match(r'^[a-zA-Z0-9._\\-]+$', skill_name), f"Skill name must match [a-zA-Z0-9._\\-], got: {skill_name!r}"
    print(f"PASS: Skill name is valid: {skill_name}")


def test_no_colon_in_skill_directory():
    """Skill directory name must not contain colons."""
    skill_dir = pathlib.Path("/var/lib/alan-portfolio/workspaces/ryan/vector-lens-144/skills/react-components")
    assert skill_dir.is_dir(), f"Skill directory must exist: {skill_dir}"
    # Directory name should not have colon
    assert ":" not in skill_dir.name, f"Skill directory name must not contain colon: {skill_dir.name!r}"
    print(f"PASS: Skill directory name is valid: {skill_dir.name}")


if __name__ == "__main__":
    test_skill_name_uses_hyphen()
    test_no_colon_in_skill_directory()
    print("\nAll tests passed!")
