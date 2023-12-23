from datadog_checks.base.utils.tagging import GENERIC_TAGS


def build_check(component, instance):
    url = instance.get(f"{component}_metric_url")
    if url is not None:
        user_tags = instance.get('tags', [])
        user_labels_mapper = instance.get('labels_mapper', {})
        user_labels_mapper.update(labels_mapper())
        instance.update(
            {
                'prometheus_url': url,
                'labels_mapper': user_labels_mapper,
                'tags': user_tags + [f'tidb_cluster_component:{component}'],
            }
        )
    return instance


def labels_mapper():
    return {label: f'{label}_in_app' for label in GENERIC_TAGS}
