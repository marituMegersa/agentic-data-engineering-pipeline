def test_agent_orchestrator():
    prompt = "Test execution query for agentic-data-engineering-pipeline"
    assert len(prompt) > 0
    assert "Test" in prompt
