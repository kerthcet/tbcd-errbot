a = {
    'taskRun': {
        'metadata': {
            'name':
            'tbcd-ci-bffql-bbjrq-notify-s2hgn',
            'namespace':
            'tekton-pipelines',
            'selfLink':
            '/apis/tekton.dev/v1alpha1/namespaces/tekton-pipelines/taskruns/tbcd-ci-bffql-bbjrq-notify-s2hgn',
            'uid':
            '7cf60200-c7a3-4d18-85f9-6d3f47900b9a',
            'resourceVersion':
            '604350698',
            'generation':
            1,
            'creationTimestamp':
            '2020-08-25T02:14:41Z',
            'labels': {
                'app.kubernetes.io/managed-by': 'tekton-pipelines',
                'tekton.dev/pipeline': 'tbcd-ci',
                'tekton.dev/pipelineRun': 'tbcd-ci-bffql-bbjrq',
                'tekton.dev/pipelineTask': 'notify',
                'tekton.dev/task': 'notify',
                'triggers.tekton.dev/eventlistener': 'tbcd',
                'triggers.tekton.dev/trigger': 'tbcd',
                'triggers.tekton.dev/triggers-eventid': 'rm8r2'
            },
            'annotations': {
                'helm.sh/hook-delete-policy':
                'before-hook-creation,hook-succeeded'
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
                'name': 'notify',
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
            'params': [{
                'name':
                'targetURL',
                'value':
                'https://oapi.dingtalk.com/robot/send?access_token=13d1c22472ad1c5b05571ff8980cc1346459bcd52ec185efc5c78002cf82a256'
            }, {
                'name':
                'repositoryURL',
                'value':
                'registry-vpc.cn-shanghai.aliyuncs.com/tiny-repo/bffql:139b385f27'
            }, {
                'name': 'project',
                'value': 'BffQL'
            }, {
                'name': 'username',
                'value': '殷纳'
            }, {
                'name': 'message',
                'value': 'add unit pricilege on unit;\n'
            }],
            'resources': {
                'outputs': [{
                    'name': 'notify',
                    'resourceSpec': {
                        'type':
                        'cloudEvent',
                        'params': [{
                            'name': 'targetURI',
                            'value': 'http://tbcd-tinybot/channel/build'
                        }]
                    },
                    'paths': ['notify/notify']
                }]
            }
        },
        'status': {
            'conditions': [{
                'type': 'Succeeded',
                'status': 'True',
                'lastTransitionTime': '2020-08-25T02:15:14Z',
                'reason': 'Succeeded',
                'message': 'All Steps have completed executing'
            }],
            'podName':
            'tbcd-ci-bffql-bbjrq-notify-s2hgn-pod-5pt2z',
            'startTime':
            '2020-08-25T02:14:41Z',
            'completionTime':
            '2020-08-25T02:15:14Z',
            'steps': [{
                'terminated': {
                    'exitCode':
                    0,
                    'reason':
                    'Completed',
                    'startedAt':
                    '2020-08-25T02:15:13Z',
                    'finishedAt':
                    '2020-08-25T02:15:13Z',
                    'containerID':
                    'docker://4d3a53bf1af2ecdbd642caf3c0071dad9ec70ec843035445887d70e727f55651'
                },
                'name':
                'echo',
                'container':
                'step-echo',
                'imageID':
                'docker-pullable://busybox@sha256:4f47c01fa91355af2865ac10fef5bf6ec9c7f42ad2321377c21e844427972977'
            }, {
                'terminated': {
                    'exitCode':
                    0,
                    'reason':
                    'Completed',
                    'startedAt':
                    '2020-08-25T02:15:12Z',
                    'finishedAt':
                    '2020-08-25T02:15:12Z',
                    'containerID':
                    'docker://a7bec3f28eab85c1281c05572c75b96bcc163859b2e02ab528ad8c30daa0aae4'
                },
                'name':
                'create-dir-notify-8wvzf',
                'container':
                'step-create-dir-notify-8wvzf',
                'imageID':
                'docker-pullable://busybox@sha256:a2490cec4484ee6c1068ba3a05f89934010c85242f736280b35343483b2264b6'
            }],
            'cloudEvents': [{
                'target': 'http://tbcd-tinybot/channel/build',
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
                    'name': 'repositoryURL',
                    'type': 'string',
                    'description': 'repository url'
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
                    'name': 'echo',
                    'image': 'busybox',
                    'resources': {},
                    'script': 'echo "Sent cloudEvent"\n'
                }]
            }
        }
    }
}
