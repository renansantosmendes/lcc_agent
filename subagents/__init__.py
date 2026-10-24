from subagents.document_analyst import document_analyst_spec


def build_subagents(model):
    """Return every subagent spec, all using the given model.

    Parameters
    ----------
    model : BaseChatModel
        Model shared by the subagents.
    """
    return [document_analyst_spec(model)]
