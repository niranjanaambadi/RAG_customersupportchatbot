from generator.prompt_template import build_prompt

def test_prompt():
    prompt = build_prompt("Reset your password via settings", "How to reset password?")
    assert "Reset your password via settings" in prompt
    assert "How to reset password?" in prompt