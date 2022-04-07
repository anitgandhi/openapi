# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.8.3, generator: @autorest/python@5.14.0)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.core.configuration import Configuration
from azure.core.pipeline import policies

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional, Union

    from azure.core.credentials import TokenCredential

VERSION = "unknown"

class DigitalOceanAPIConfiguration(Configuration):  # pylint: disable=too-many-instance-attributes
    """Configuration for DigitalOceanAPI.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param ssh_key_identifier: Either the ID or the fingerprint of an existing SSH key.
    :type ssh_key_identifier: any
    :param action_id: A unique numeric ID that can be used to identify and reference an action.
    :type action_id: int
    :param id: The ID of the app.
    :type id: str
    :param app_id: The app ID.
    :type app_id: str
    :param deployment_id: The deployment ID.
    :type deployment_id: str
    :param component_name: An optional component name. If set, logs will be limited to this
     component only.
    :type component_name: str
    :param slug: The slug of the tier.
    :type slug: str
    :param alert_id: The alert ID.
    :type alert_id: str
    :param cdn_id: A unique identifier for a CDN endpoint.
    :type cdn_id: str
    :param certificate_id: A unique identifier for a certificate.
    :type certificate_id: str
    :param invoice_uuid: UUID of the invoice.
    :type invoice_uuid: str
    :param database_cluster_uuid: A unique identifier for a database cluster.
    :type database_cluster_uuid: str
    :param migration_id: A unique identifier assigned to the online migration.
    :type migration_id: str
    :param replica_name: The name of the database replica.
    :type replica_name: str
    :param username: The name of the database user.
    :type username: str
    :param database_name: The name of the database.
    :type database_name: str
    :param pool_name: The name used to identify the connection pool.
    :type pool_name: str
    :param domain_name: The name of the domain itself.
    :type domain_name: str
    :param domain_record_id: The unique identifier of the domain record.
    :type domain_record_id: int
    :param droplet_id: A unique identifier for a Droplet instance.
    :type droplet_id: int
    :param x_dangerous: Acknowledge this action will destroy the Droplet and all associated
     resources and *can not* be reversed.
    :type x_dangerous: bool
    :param firewall_id: A unique ID that can be used to identify and reference a firewall.
    :type firewall_id: str
    :param floating_ip: A floating IP address.
    :type floating_ip: str
    :param image_id: A unique number that can be used to identify and reference a specific image.
    :type image_id: int
    :param cluster_id: A unique ID that can be used to reference a Kubernetes cluster.
    :type cluster_id: str
    :param node_pool_id: A unique ID that can be used to reference a Kubernetes node pool.
    :type node_pool_id: str
    :param node_id: A unique ID that can be used to reference a node in a Kubernetes node pool.
    :type node_id: str
    :param lb_id: A unique identifier for a load balancer.
    :type lb_id: str
    :param alert_uuid: A unique identifier for an alert policy.
    :type alert_uuid: str
    :param host_id: The droplet ID.
    :type host_id: str
    :param interface: The network interface.
    :type interface: str or ~digital_ocean_api.models.Enum69
    :param direction: The traffic direction.
    :type direction: str or ~digital_ocean_api.models.Enum70
    :param start: Timestamp to start metric window.
    :type start: str
    :param end: Timestamp to end metric window.
    :type end: str
    :param project_id: A unique identifier for a project.
    :type project_id: str
    :param registry_name: The name of a container registry.
    :type registry_name: str
    :param repository_name: The name of a container registry repository. If the name contains ``/``
     characters, they must be URL-encoded, e.g. ``%2F``.
    :type repository_name: str
    :param repository_tag: The name of a container registry repository tag.
    :type repository_tag: str
    :param manifest_digest: The manifest digest of a container registry repository tag.
    :type manifest_digest: str
    :param garbage_collection_uuid: The UUID of a garbage collection run.
    :type garbage_collection_uuid: str
    :param snapshot_id: Either the ID of an existing snapshot. This will be an integer for a
     Droplet snapshot or a string for a volume snapshot.
    :type snapshot_id: any
    :param tag_id: The name of the tag. Tags may contain letters, numbers, colons, dashes, and
     underscores. There is a limit of 255 characters per tag.
    :type tag_id: str
    :param volume_id: The ID of the block storage volume.
    :type volume_id: str
    :param vpc_id: A unique identifier for a VPC.
    :type vpc_id: str
    :param type: Restrict results to a certain type of 1-Click. Default value is None.
    :type type: str or ~digital_ocean_api.models.Enum0
    :param per_page: Number of items returned per page. Default value is 20.
    :type per_page: int
    :param page: Which 'page' of paginated results to return. Default value is 1.
    :type page: int
    :param name: The name of the app to retrieve. Default value is None.
    :type name: str
    :param follow: Whether the logs should follow live updates. Default value is None.
    :type follow: bool
    :param pod_connection_timeout: An optional time duration to wait if the underlying component
     instance is not immediately available. Default: ``3m``. Default value is None.
    :type pod_connection_timeout: str
    :param tag_name: Limits the results to database clusters with a specific tag. Default value is
     None.
    :type tag_name: str
    :param private: Used to filter only user images. Default value is None.
    :type private: bool
    :param expiry_seconds: The duration in seconds that the returned Kubernetes credentials will be
     valid. If not set or 0, the credentials will have a 7 day expiry. Default value is 0.
    :type expiry_seconds: int
    :param skip_drain: Specifies whether or not to drain workloads from a node before it is
     deleted. Setting it to ``1`` causes node draining to be skipped. Omitting the query parameter
     or setting its value to ``0`` carries out draining prior to deletion. Default value is 0.
    :type skip_drain: int
    :param replace: Specifies whether or not to replace a node after it has been deleted. Setting
     it to ``1`` causes the node to be replaced by a new one after deletion. Omitting the query
     parameter or setting its value to ``0`` deletes without replacement. Default value is 0.
    :type replace: int
    :param run_id: Specifies the clusterlint run whose results will be retrieved. Default value is
     None.
    :type run_id: str
    :param read_write: By default, the registry credentials allow for read-only access. Set this
     query parameter to ``true`` to obtain read-write credentials. Default value is False.
    :type read_write: bool
    :param page_token: Token to retrieve of the next or previous set of results more quickly than
     using 'page'. Default value is None.
    :type page_token: str
    :param resource_type: Used to filter snapshots by a resource type. Default value is None.
    :type resource_type: str or ~digital_ocean_api.models.Enum79
    :param region: The slug identifier for the region where the resource is available. Default
     value is None.
    :type region: str or ~digital_ocean_api.models.RegionSlug
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        ssh_key_identifier,  # type: Any
        action_id,  # type: int
        id,  # type: str
        app_id,  # type: str
        deployment_id,  # type: str
        component_name,  # type: str
        slug,  # type: str
        alert_id,  # type: str
        cdn_id,  # type: str
        certificate_id,  # type: str
        invoice_uuid,  # type: str
        database_cluster_uuid,  # type: str
        migration_id,  # type: str
        replica_name,  # type: str
        username,  # type: str
        database_name,  # type: str
        pool_name,  # type: str
        domain_name,  # type: str
        domain_record_id,  # type: int
        droplet_id,  # type: int
        x_dangerous,  # type: bool
        firewall_id,  # type: str
        floating_ip,  # type: str
        image_id,  # type: int
        cluster_id,  # type: str
        node_pool_id,  # type: str
        node_id,  # type: str
        lb_id,  # type: str
        alert_uuid,  # type: str
        host_id,  # type: str
        interface,  # type: Union[str, "_models.Enum69"]
        direction,  # type: Union[str, "_models.Enum70"]
        start,  # type: str
        end,  # type: str
        project_id,  # type: str
        registry_name,  # type: str
        repository_name,  # type: str
        repository_tag,  # type: str
        manifest_digest,  # type: str
        garbage_collection_uuid,  # type: str
        snapshot_id,  # type: Any
        tag_id,  # type: str
        volume_id,  # type: str
        vpc_id,  # type: str
        type=None,  # type: Optional[Union[str, "_models.Enum0"]]
        per_page=20,  # type: Optional[int]
        page=1,  # type: Optional[int]
        name=None,  # type: Optional[str]
        follow=None,  # type: Optional[bool]
        pod_connection_timeout=None,  # type: Optional[str]
        tag_name=None,  # type: Optional[str]
        private=None,  # type: Optional[bool]
        expiry_seconds=0,  # type: Optional[int]
        skip_drain=0,  # type: Optional[int]
        replace=0,  # type: Optional[int]
        run_id=None,  # type: Optional[str]
        read_write=False,  # type: Optional[bool]
        page_token=None,  # type: Optional[str]
        resource_type=None,  # type: Optional[Union[str, "_models.Enum79"]]
        region=None,  # type: Optional[Union[str, "_models.RegionSlug"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        super(DigitalOceanAPIConfiguration, self).__init__(**kwargs)
        if credential is None:
            raise ValueError("Parameter 'credential' must not be None.")
        if ssh_key_identifier is None:
            raise ValueError("Parameter 'ssh_key_identifier' must not be None.")
        if action_id is None:
            raise ValueError("Parameter 'action_id' must not be None.")
        if id is None:
            raise ValueError("Parameter 'id' must not be None.")
        if app_id is None:
            raise ValueError("Parameter 'app_id' must not be None.")
        if deployment_id is None:
            raise ValueError("Parameter 'deployment_id' must not be None.")
        if component_name is None:
            raise ValueError("Parameter 'component_name' must not be None.")
        if slug is None:
            raise ValueError("Parameter 'slug' must not be None.")
        if alert_id is None:
            raise ValueError("Parameter 'alert_id' must not be None.")
        if cdn_id is None:
            raise ValueError("Parameter 'cdn_id' must not be None.")
        if certificate_id is None:
            raise ValueError("Parameter 'certificate_id' must not be None.")
        if invoice_uuid is None:
            raise ValueError("Parameter 'invoice_uuid' must not be None.")
        if database_cluster_uuid is None:
            raise ValueError("Parameter 'database_cluster_uuid' must not be None.")
        if migration_id is None:
            raise ValueError("Parameter 'migration_id' must not be None.")
        if replica_name is None:
            raise ValueError("Parameter 'replica_name' must not be None.")
        if username is None:
            raise ValueError("Parameter 'username' must not be None.")
        if database_name is None:
            raise ValueError("Parameter 'database_name' must not be None.")
        if pool_name is None:
            raise ValueError("Parameter 'pool_name' must not be None.")
        if domain_name is None:
            raise ValueError("Parameter 'domain_name' must not be None.")
        if domain_record_id is None:
            raise ValueError("Parameter 'domain_record_id' must not be None.")
        if droplet_id is None:
            raise ValueError("Parameter 'droplet_id' must not be None.")
        if x_dangerous is None:
            raise ValueError("Parameter 'x_dangerous' must not be None.")
        if firewall_id is None:
            raise ValueError("Parameter 'firewall_id' must not be None.")
        if floating_ip is None:
            raise ValueError("Parameter 'floating_ip' must not be None.")
        if image_id is None:
            raise ValueError("Parameter 'image_id' must not be None.")
        if cluster_id is None:
            raise ValueError("Parameter 'cluster_id' must not be None.")
        if node_pool_id is None:
            raise ValueError("Parameter 'node_pool_id' must not be None.")
        if node_id is None:
            raise ValueError("Parameter 'node_id' must not be None.")
        if lb_id is None:
            raise ValueError("Parameter 'lb_id' must not be None.")
        if alert_uuid is None:
            raise ValueError("Parameter 'alert_uuid' must not be None.")
        if host_id is None:
            raise ValueError("Parameter 'host_id' must not be None.")
        if interface is None:
            raise ValueError("Parameter 'interface' must not be None.")
        if direction is None:
            raise ValueError("Parameter 'direction' must not be None.")
        if start is None:
            raise ValueError("Parameter 'start' must not be None.")
        if end is None:
            raise ValueError("Parameter 'end' must not be None.")
        if project_id is None:
            raise ValueError("Parameter 'project_id' must not be None.")
        if registry_name is None:
            raise ValueError("Parameter 'registry_name' must not be None.")
        if repository_name is None:
            raise ValueError("Parameter 'repository_name' must not be None.")
        if repository_tag is None:
            raise ValueError("Parameter 'repository_tag' must not be None.")
        if manifest_digest is None:
            raise ValueError("Parameter 'manifest_digest' must not be None.")
        if garbage_collection_uuid is None:
            raise ValueError("Parameter 'garbage_collection_uuid' must not be None.")
        if snapshot_id is None:
            raise ValueError("Parameter 'snapshot_id' must not be None.")
        if tag_id is None:
            raise ValueError("Parameter 'tag_id' must not be None.")
        if volume_id is None:
            raise ValueError("Parameter 'volume_id' must not be None.")
        if vpc_id is None:
            raise ValueError("Parameter 'vpc_id' must not be None.")

        self.credential = credential
        self.ssh_key_identifier = ssh_key_identifier
        self.action_id = action_id
        self.id = id
        self.app_id = app_id
        self.deployment_id = deployment_id
        self.component_name = component_name
        self.slug = slug
        self.alert_id = alert_id
        self.cdn_id = cdn_id
        self.certificate_id = certificate_id
        self.invoice_uuid = invoice_uuid
        self.database_cluster_uuid = database_cluster_uuid
        self.migration_id = migration_id
        self.replica_name = replica_name
        self.username = username
        self.database_name = database_name
        self.pool_name = pool_name
        self.domain_name = domain_name
        self.domain_record_id = domain_record_id
        self.droplet_id = droplet_id
        self.x_dangerous = x_dangerous
        self.firewall_id = firewall_id
        self.floating_ip = floating_ip
        self.image_id = image_id
        self.cluster_id = cluster_id
        self.node_pool_id = node_pool_id
        self.node_id = node_id
        self.lb_id = lb_id
        self.alert_uuid = alert_uuid
        self.host_id = host_id
        self.interface = interface
        self.direction = direction
        self.start = start
        self.end = end
        self.project_id = project_id
        self.registry_name = registry_name
        self.repository_name = repository_name
        self.repository_tag = repository_tag
        self.manifest_digest = manifest_digest
        self.garbage_collection_uuid = garbage_collection_uuid
        self.snapshot_id = snapshot_id
        self.tag_id = tag_id
        self.volume_id = volume_id
        self.vpc_id = vpc_id
        self.type = type
        self.per_page = per_page
        self.page = page
        self.name = name
        self.follow = follow
        self.pod_connection_timeout = pod_connection_timeout
        self.tag_name = tag_name
        self.private = private
        self.expiry_seconds = expiry_seconds
        self.skip_drain = skip_drain
        self.replace = replace
        self.run_id = run_id
        self.read_write = read_write
        self.page_token = page_token
        self.resource_type = resource_type
        self.region = region
        self.credential_scopes = kwargs.pop('credential_scopes', [])
        kwargs.setdefault('sdk_moniker', 'digitaloceanapi/{}'.format(VERSION))
        self._configure(**kwargs)

    def _configure(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        self.user_agent_policy = kwargs.get('user_agent_policy') or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get('headers_policy') or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get('proxy_policy') or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get('logging_policy') or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.http_logging_policy = kwargs.get('http_logging_policy') or policies.HttpLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get('retry_policy') or policies.RetryPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get('custom_hook_policy') or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get('redirect_policy') or policies.RedirectPolicy(**kwargs)
        self.authentication_policy = kwargs.get('authentication_policy')
        if not self.credential_scopes and not self.authentication_policy:
            raise ValueError("You must provide either credential_scopes or authentication_policy as kwargs")
        if self.credential and not self.authentication_policy:
            self.authentication_policy = policies.BearerTokenCredentialPolicy(self.credential, *self.credential_scopes, **kwargs)
