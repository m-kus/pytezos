from os.path import join

import requests


def create_deployment(repo_slug, oauth_token, environment, ref='master'):
    return requests.post(
        url=join('https://api.github.com/repos', repo_slug, 'deployments'),
        headers={
            'Accept': 'application/vnd.github.ant-man-preview+json',
            'Authorization': f'token {oauth_token}',
        },
        json={
            'ref': ref,
            'environment': environment,
            'required_contexts': [],
        },  # bypass checking
    ).json()


def create_deployment_status(repo_slug, oauth_token, deployment_id, state, environment, environment_url=None):
    assert state in {'success', 'failure'}
    return requests.post(
        url=join('https://api.github.com/repos', repo_slug, 'deployments', str(deployment_id), 'statuses'),
        headers={
            'Accept': 'application/vnd.github.flash-preview+json',
            'Authorization': f'token {oauth_token}',
        },
        json={
            'state': state,
            'environment': environment,
            'environment_url': environment_url,
        },
    ).json()
