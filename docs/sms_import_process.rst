AWS Server Migration Service (SMS)
===================================

**Context:**
 Facilitating the Import of a Virtual Machines into AWS with the emphisis on mass migration of all of UCOP's virtual environment located on-premise.


**Goals:**
 This initial draft seeks to explain the migration process of AWS Server Migration Service and how it will help with the ability to do a 'lift and shit' of an On-Premise virtual environment to an AWS environment.

What is SMS:
-------------------------
- AWS Server Migration Service (SMS) is an agentless service which makes it easier and faster for you to migrate thousands of on-premises workloads to AWS. AWS SMS allows you to automate, schedule, and track incremental replications of live server volumes, making it easier for you to coordinate large-scale server migrations.


What functionality is provided:
-------------------------------
-  AWS SMS has been desgined to integrate directly with VMware Vsphere. It allows users to replicate virtual machines that are live and in service via the VMWare snapshot technology.  Since the VM does not require to be powered off, instead a replication process is initiated from on-premise to AWS. This process can be configured to be a one-time replication or setup to replicate on a schedule till the time arrives where the VM will fully be migrated to AWS and removed from on-premise's inventory. 


How is SMS used:
--------------------------
- SMS can be used either in the CONSOLE or via CLI. 
- The integration between VMWare and AWS, the following technologies are used
- Snapshot Technology
- Replication Technology 
- VMWare Vcenter
- AWS Services
- Up to 50 concurent replication process supported


**Walk-thru** of utilizing AWS Server Migration Service (SMS):
--------------------------------------------

- Import catalog of virtual machines from the on-premise VMWare environment setup
::

	aws sms import-server-catalog --region us-west-2
	
- Find Virtual machine you want to migrate
::

	aws sms get-servers  |grep -B 10 awsscrum-lnx1
            }
        },
        {
            "serverId": "s-4e856027",
            "serverType": "VIRTUAL_MACHINE",
            "vmServer": {
                "vmServerAddress": {
                    "vmManagerId": "8DA3177D-A94E-4989-80E0-EE8A8A2E9586",
                    "vmId": "vm-188760"
                },
                "vmName": "awsscrum-lnx1",
                "vmManagerName": "p-sdsc-vcenter1.ucop.edu",
                "vmManagerType": "vSphere",
                "vmPath": "/Datacenters/SDSC/vm/awsscrum-lnx1"

- Locate *server-Id*
::

	"serverId": "s-4e856027",

- Start initial seed replication of virtual machine
::	

	aws sms create-replication-job  --server-id s-4e856027 --role-name sms  --description "Demo moving VM to AWS using SMS Service " --seed-replication-time 2018-11-07T09:48-08:00  --frequency 12 --region us-west-2

- Verify replication runs based of *replication job id*
::

	aws sms get-replication-runs --replication-job-id "sms-job-5691743f" --region us-west-2
	{
    "replicationRunList": [
        {
            "replicationRunId": "sms-run-12688d7b",
            "state": "Pending",
            "type": "Automatic",
            "scheduledStartTime": 1541916600.0
        },
        {
            "replicationRunId": "sms-run-56688d3f",
            "state": "Completed",
            "type": "Automatic",
            "amiId": "ami-0f988515e7d6730eb",
            "scheduledStartTime": 1541873400.0,
            "completedTime": 1541876322.298
        },
        {
            "replicationRunId": "sms-run-7a688d13",
            "state": "Completed",
            "type": "Automatic",
            "amiId": "ami-0867f285b248cfb0f",
            "scheduledStartTime": 1541830200.0,
            "completedTime": 1541840044.194
        }
    ]
}

- *NOTE* The above will take an undetermined amount of time to complete, therefore this process must be done with a possible significant delay between steps depending on the number of concurent replications.

Additional pertinent and useful commands
--------------------------------------

- *NOTE* - Per the AWS documentation there are *NO* CLI commands available to install and configure the connector

- Update replication after initial seed has completed
::

	 aws sms update-replication-job --region us-west-2 --replication-job-id sms-job-436r4372 --frequency 24 --next-replication-run-start-time 2018-11-06T15:30:00-07:00

- Initiate *on-demand* replication
::

	aws sms start-on-demand-replication-run --replication-job-id sms-job-436r4372 --region us-west-2

- Delete replication jobs no longer required - house keeping cleanup
::

	aws sms delete-replication-job --region us-west-2 --replication-job-id sms-job-436r4372

- Delete server catalog tht has been pulled from the on-premise datacenter(SDSC)
::

	aws sms delete-server-catalog --region us-west-2

- Disassociate connector from the on-premise datacenter (SDSC)
::

	aws sms disassociate-connector --region us-east-1 --connector-id c-415fef98f4c66c487 


Pre-requirements for using the Server Migration Service (SMS)
==========================================================


OS Supported based off UCOP's current list
------------------------------------------
- Microsoft Windows Server 2003 (Standard, Datacenter, Enterprise) with Service Pack 1 (SP1) or later (32- and 64-bit)
- Microsoft Windows Server 2003 R2 (Standard, Datacenter, Enterprise) (32- and 64-bit)
- Microsoft Windows Server 2008 (Standard, Datacenter, Enterprise) (32- and 64-bit)
- Microsoft Windows Server 2008 R2 (Standard, Datacenter, Enterprise) (64-bit only)
- Microsoft Windows Server 2012 (Standard, Datacenter) (64-bit only)
- Microsoft Windows Server 2012 R2 (Standard, Datacenter) (64-bit only) (Nano Server installation not supported)
- Microsoft Windows Server 2016 (Standard, Datacenter) (64-bit only)

- Red Hat Enterprise Linux (RHEL) 5.1-5.11, 6.1-6.9, 7.0-7.3 (6.0 lacks required drivers)
- SUSE Linux Enterprise Server 11 with Service Pack 1 and kernel 2.6.32.12-0.7
- SUSE Linux Enterprise Server 11 with Service Pack 2 and kernel 3.0.13-0.27
- SUSE Linux Enterprise Server 11 with Service Pack 3 and kernel 3.0.76-0.11, 3.0.101-0.8, or 3.0.101-0.15
- SUSE Linux Enterprise Server 11 with Service Pack 4 and kernel 3.0.101-63
- SUSE Linux Enterprise Server 12 with kernel 3.12.28-4

Licensing Information
=====================

Licensing for Windows
---------------------
- Windows server operating systems support either BYOL or AWS licenses. Windows client operating systems (such as Windows 10) support only BYOL licenses.

- If you choose Auto (the default), AWS SMS uses the AWS license if the VM has a server OS. Otherwise, the BYOL license is used.



Licensing for Linux
-------------------

- Linux operating systems support only BYOL licenses. Choosing Auto (the default) means that AWS SMS uses a BYOL license.

- Migrated Red Hat Enterprise Linux (RHEL) VMs must use Cloud Access (BYOL) licenses. For more information, see Red Hat Cloud Access on the Red Hat website.

- Migrated SUSE Linux Enterprise Server VMs must use SUSE Public Cloud Program (BYOS) licenses. For more information, see SUSE Public Cloud Program—Bring Your Own Subscription.


Important Information
=====================

- AWS Server Migration Service partially supports vMotion, Storage vMotion, and other features based on virtual machine migration (such as DRS and Storage DRS) subject to the following limitations:

- Migrating a virtual machine to a new ESXi host or datastore after one replication run ends, and before the next replication run begins, is supported as long as the Server Migration Connector's vCenter service account has sufficient permissions on the destination ESXi host, datastores, and datacenter, and on the virtual machine itself at the new location.

- Migrating a virtual machine to a new ESXi host, datastore, and/or datacenter while a replication run is active—that is, while a virtual machine upload is in progress—is not supported.

- Cross vCenter vMotion is not supported for use with the AWS Server Migration Service.
