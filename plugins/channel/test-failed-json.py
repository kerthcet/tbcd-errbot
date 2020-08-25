a = {
    'taskRun': {
        'metadata': {
            'name':
            'tbcd-ci-accountservice-444fg-automated-testing-ncfhj',
            'namespace':
            'tekton-pipelines',
            'selfLink':
            '/apis/tekton.dev/v1alpha1/namespaces/tekton-pipelines/taskruns/tbcd-ci-accountservice-444fg-automated-testing-ncfhj',
            'uid':
            '5bf0a499-2adf-4b2d-9c6e-365a1c308a6e',
            'resourceVersion':
            '606022187',
            'generation':
            1,
            'creationTimestamp':
            '2020-08-25T06:25:25Z',
            'labels': {
                'app.kubernetes.io/managed-by': 'tekton-pipelines',
                'tekton.dev/pipeline': 'tbcd-ci',
                'tekton.dev/pipelineRun': 'tbcd-ci-accountservice-444fg',
                'tekton.dev/pipelineTask': 'automated-testing',
                'tekton.dev/task': 'automated-testing',
                'triggers.tekton.dev/eventlistener': 'tbcd',
                'triggers.tekton.dev/trigger': 'tbcd',
                'triggers.tekton.dev/triggers-eventid': 'kcms8'
            },
            'ownerReferences': [{
                'apiVersion': 'tekton.dev/v1alpha1',
                'kind': 'PipelineRun',
                'name': 'tbcd-ci-accountservice-444fg',
                'uid': '9a35b12a-a38a-4514-bf8f-46a76946b960',
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
                    'claimName':
                    'git-shared-data-project-tbcd-ci-accountservice-444fg'
                }
            }],
            'params': [{
                'name':
                'targetURL',
                'value':
                'https://oapi.dingtalk.com/robot/send?access_token=13d1c22472ad1c5b05571ff8980cc1346459bcd52ec185efc5c78002cf82a256'
            }, {
                'name': 'project',
                'value': 'AccountService'
            }, {
                'name': 'username',
                'value': '殷纳'
            }, {
                'name': 'message',
                'value': 'test\n'
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
                'type':
                'Succeeded',
                'status':
                'False',
                'lastTransitionTime':
                '2020-08-25T06:26:56Z',
                'reason':
                'Failed',
                'message':
                '"step-run-test" exited with code 2 (image: "docker-pullable://golang@sha256:4c3279e05a0131c0565466ac538755f104d8d936efbc4c30ba7d717c73f3e2c2"); for logs run: kubectl -n tekton-pipelines logs tbcd-ci-accountservice-444fg-automated-testing-ncfhj-pod-hrdcm -c step-run-test\\n'
            }],
            'podName':
            'tbcd-ci-accountservice-444fg-automated-testing-ncfhj-pod-hrdcm',
            'startTime':
            '2020-08-25T06:25:25Z',
            'completionTime':
            '2020-08-25T06:26:56Z',
            'steps': [{
                'terminated': {
                    'exitCode':
                    2,
                    'reason':
                    'Error',
                    'startedAt':
                    '2020-08-25T06:26:11Z',
                    'finishedAt':
                    '2020-08-25T06:26:55Z',
                    'containerID':
                    'docker://8b3d3896867c6a2dee52d66f441c1f1d97e503c489c69075767719c6b5f6a39b'
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
                    '2020-08-25T06:26:10Z',
                    'finishedAt':
                    '2020-08-25T06:26:10Z',
                    'containerID':
                    'docker://9ac92fdc2671eebd9bb562f5ad86ba30fb13fa8a7d59eabe5665ff9e1a48c61c'
                },
                'name':
                'create-dir-notify-zvc44',
                'container':
                'step-create-dir-notify-zvc44',
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
                'params': [{
                    'name': 'targetURL',
                    'type': 'string',
                    'description': 'notify target url'
                }, {
                    'name': 'project',
                    'type': 'string',
                    'description': 'project name'
                }, {
                    'name': 'username',
                    'type': 'string',
                    'description': 'commit username'
                }, {
                    'name': 'message',
                    'type': 'string',
                    'description': 'commit message'
                }],
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
