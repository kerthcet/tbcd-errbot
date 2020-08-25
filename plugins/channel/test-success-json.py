a = {
    'taskRun': {
        'metadata': {
            'name':
            'tbcd-ci-bffql-bbjrq-automated-testing-fqdt2',
            'namespace':
            'tekton-pipelines',
            'selfLink':
            '/apis/tekton.dev/v1alpha1/namespaces/tekton-pipelines/taskruns/tbcd-ci-bffql-bbjrq-automated-testing-fqdt2',
            'uid':
            '7be512f7-adcf-45d7-92fa-cd75990400a9',
            'resourceVersion':
            '604327766',
            'generation':
            1,
            'creationTimestamp':
            '2020-08-25T02:10:14Z',
            'labels': {
                'app.kubernetes.io/managed-by': 'tekton-pipelines',
                'tekton.dev/pipeline': 'tbcd-ci',
                'tekton.dev/pipelineRun': 'tbcd-ci-bffql-bbjrq',
                'tekton.dev/pipelineTask': 'automated-testing',
                'tekton.dev/task': 'automated-testing',
                'triggers.tekton.dev/eventlistener': 'tbcd',
                'triggers.tekton.dev/trigger': 'tbcd',
                'triggers.tekton.dev/triggers-eventid': 'rm8r2'
            },
            'ownerReferences': [{
                'apiVersion': 'tekton.dev/v1alpha1',
                'kind': 'PipelineRun',
                'name': 'tbcd-ci-bffql-bbjrq',
                'uid': 'bbd05fb4-2fd8-49f3-b51c-e91a2f68c76a',
                'controller': True,
                'blockOwnerDeletion': True
            }]
        },
        'spec': {
            'serviceAccountName':
            'tekton-triggers-admin',
            'taskRef': {
                'name': 'automated-testing',
                'kind': 'Task'
            },
            'timeout':
            '1h0m0s',
            'podTemplate': {
                'nodeSelector': {
                    'node-role.kubernetes.io/devops': 'tbcd'
                },
                'schedulerName': '',
                'hostNetwork': False
            },
            'workspaces': [{
                'name': 'source',
                'persistentVolumeClaim': {
                    'claimName': 'git-shared-data-project-tbcd-ci-bffql-bbjrq'
                }
            }],
            'resources': {
                'outputs': [{
                    'name': 'notify',
                    'resourceSpec': {
                        'type':
                        'cloudEvent',
                        'params': [{
                            'name': 'targetURI',
                            'value': 'http://tbcd-tinybot/channel/test'
                        }]
                    },
                    'paths': ['automated-testing/notify']
                }]
            }
        },
        'status': {
            'conditions': [{
                'type': 'Succeeded',
                'status': 'True',
                'lastTransitionTime': '2020-08-25T02:11:46Z',
                'reason': 'Succeeded',
                'message': 'All Steps have completed executing'
            }],
            'podName':
            'tbcd-ci-bffql-bbjrq-automated-testing-fqdt2-pod-68kgq',
            'startTime':
            '2020-08-25T02:10:14Z',
            'completionTime':
            '2020-08-25T02:11:46Z',
            'steps': [{
                'terminated': {
                    'exitCode':
                    0,
                    'reason':
                    'Completed',
                    'startedAt':
                    '2020-08-25T02:10:50Z',
                    'finishedAt':
                    '2020-08-25T02:11:44Z',
                    'containerID':
                    'docker://43a3dd7ce10866aef0c1a9148b809af56f406ce4f6bc916bf67105b3a836eb1f'
                },
                'name':
                'run-test',
                'container':
                'step-run-test',
                'imageID':
                'docker-pullable://golang@sha256:4c3279e05a0131c0565466ac538755f104d8d936efbc4c30ba7d717c73f3e2c2'
            }, {
                'terminated': {
                    'exitCode':
                    0,
                    'reason':
                    'Completed',
                    'startedAt':
                    '2020-08-25T02:10:49Z',
                    'finishedAt':
                    '2020-08-25T02:10:49Z',
                    'containerID':
                    'docker://a9140bc2487669449cab1bef2ee170d39ea3cb5b7f130568cf38f96d96d694e1'
                },
                'name':
                'create-dir-notify-d6gnx',
                'container':
                'step-create-dir-notify-d6gnx',
                'imageID':
                'docker-pullable://busybox@sha256:a2490cec4484ee6c1068ba3a05f89934010c85242f736280b35343483b2264b6'
            }],
            'cloudEvents': [{
                'target': 'http://tbcd-tinybot/channel/test',
                'status': {
                    'condition': 'Unknown',
                    'message': '',
                    'retryCount': 0
                }
            }],
            'taskSpec': {
                'resources': {
                    'outputs': [{
                        'name': 'notify',
                        'type': 'cloudEvent'
                    }]
                },
                'steps': [{
                    'name':
                    'run-test',
                    'image':
                    'golang',
                    'workingDir':
                    '$(workspaces.source.path)',
                    'resources': {},
                    'volumeMounts': [{
                        'name': 'test-reports',
                        'mountPath': '/test-reports'
                    }],
                    'script':
                    '#!/bin/bash\n# golang related\nexport GOPROXY=https://goproxy.cn\nexport GO111MODULE=on\n\nmake test\n'
                }],
                'volumes': [{
                    'name': 'test-reports',
                    'persistentVolumeClaim': {
                        'claimName': 'test-reports'
                    }
                }],
                'workspaces': [{
                    'name':
                    'source',
                    'description':
                    'A workspace that contains the fetched git repository.'
                }]
            }
        }
    }
}
