def test_import_supervisor_runs():
    from agent.supervisor import run
    assert run() == "supervisor running"
