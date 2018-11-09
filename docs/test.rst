VM Import/Export Solution Migration
===================================

**Context:**
 Facilitating the Import of a Virtual Machines into AWS as a way to satisfy multiple requirements such as migrations of smalle
 r scoped environments,  ensure Disaster Recovery and/or Backups of system or application data is captured.


**Goals:**
 This initial draft seeks to discover different methos of moving Virtual Machines or application data from an On-Premise farm
 to aand AWS account.

What is VM Import/Export:
-------------------------
- VM Import/Export enables you to import virtual machine (VM) images from your existing virtualization environment to Amazon EC2, and then export them back.


What functionality is provided:
-------------------------------
- The ability to import a VM from your virtualization environment to Amazon EC2 as an Amazon Machine Image (AMI). You can launch EC2 instances from your AMI any time.



Types of VM Import/Export:
--------------------------
- Image import  ( supports Multi-disk imports and Windows BYOL)
- Instance import ( Multi-disk imports and Windows BYOL)
- Snapshot Import ( Import a VMDK and create and EBS volume than attach to an EC2 Instance)

