# -*- coding: utf-8 -*-

from cdpy.common import CdpSdkBase, Squelch, CdpcliWrapper

class CdpyDe(CdpSdkBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def describe_vc(self, cluster_id, vc_id):
        return self.sdk.call(
            svc='de', func='describe_vc', ret_field='vc', squelch=[
                Squelch('NOT_FOUND'), Squelch('INVALID_ARGUMENT')
            ],
            clusterId=cluster_id,
            vcId=vc_id
        )

    def list_vcs(self, cluster_id):
         return self.sdk.call(
            svc='de', func='list_vcs', ret_field='vcs', squelch=[
                Squelch(value='NOT_FOUND', default=list()),
                Squelch(field='status_code', value='504', default=list(),
                        warning="No VCS in this Cluster"),
            ],
            clusterId=cluster_id
        )

    def create_vc(self, name, cluster_id, cpu_requests, memory_requests,
                  chart_value_overrides=None, runtime_spot_component=None):
        return self.sdk.call(
            svc='de', func='create_vc', ret_field='Vc',
            name=name,
            clusterId=cluster_id,
            cpuRequests=cpu_requests,
            memoryRequests=memory_requests,
            chartValueOverrides=chart_value_overrides,
            runtimeSpotComponent=runtime_spot_component
        )

    def delete_vc(self, cluster_id, vc_id):
        return self.sdk.call(
            svc='de', func='delete_vc', ret_field='status', squelch=[Squelch('NOT_FOUND')],
            clusterId=cluster_id, vcId=vc_id
        )

    def describe_service(self, cluster_id):
        return self.sdk.call(
            svc='de', func='describe_service', ret_field='service', squelch=[
                Squelch('NOT_FOUND'), Squelch('INVALID_ARGUMENT')
            ],
            clusterId=cluster_id,
        )

    def list_services(self, env=None, remove_deleted=False):
        services = self.sdk.call(
            svc='de', func='list_services', ret_field='services', squelch=[
                Squelch(value='NOT_FOUND', default=list())], removeDeleted=remove_deleted
        )
        return [s for s in services if env is None or s['environmentName'] == env]

    def enable_service(self, name, env, instance_type, minimum_instances, maximum_instances, 
            initial_instances=None, minimum_spot_instances=None, maximum_spot_instances=None, 
            initial_spot_instances=None, chart_value_overrides=None, enable_public_endpoint=False,
            enable_workload_analytics=False, root_volume_size=None, skip_validation=False,
            tags=None, use_ssd=False, whitelist_ips=None):
        return self.sdk.call(
            svc='de', func='enable_service', ret_field='service',
            name=name,
            env=env,
            instanceType=instance_type,
            minimumInstances=minimum_instances,
            maximumInstances=maximum_instances,
            initialInstances=initial_instances,
            minimumSpotInstances=minimum_spot_instances,
            maximumSpotInstances=maximum_spot_instances,
            initialSpotInstances=initial_spot_instances,
            chartValueOverrides=chart_value_overrides,
            enablePublicEndpoint=enable_public_endpoint,
            enableWorkloadAnalytics=enable_workload_analytics,
            rootVolumeSize=root_volume_size,
            skipValidation=skip_validation,
            tags=tags,
            useSsd=use_ssd,
            whitelistIps=whitelist_ips
        )

    def disable_service(self, cluster_id, force=False):
        return self.sdk.call(
            svc='de', func='disable_service', ret_field='status', squelch=[Squelch('NOT_FOUND')], 
            clusterId=cluster_id, force=force
        )

    def get_kubeconfig(self, cluster_id):
        return self.sdk.call(
            svc='de', func='get_kubeconfig', ret_field='kubeconfig', squelch=[Squelch('NOT_FOUND')],
            clusterId=cluster_id
        )
