from robusta.api import *

# TODO: merge with node_status_enricher?
@action
def deployment_status_enricher(event: DeploymentEvent):
    """
    Enrich the finding with deployment status conditions.

    Usually these conditions can provide important information regarding possible issues.
    """
    deployment = event.get_deployment()
    if not deployment:
        logging.error(
            f"cannot run deployment_status_enricher on event with no deployment: {event}"
        )
        return

    block_list: List[BaseBlock] = [MarkdownBlock("*Deployment status details:*")]
    block_list.extend(
        MarkdownBlock(f"*{condition.reason} -* {condition.message}")
        for condition in deployment.status.conditions
    )

    event.add_enrichment(block_list)
