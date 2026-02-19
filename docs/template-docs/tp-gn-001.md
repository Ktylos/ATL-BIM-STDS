# ATL-STD-XX-TP-GN-001: BIM Execution Plan Template

!!! info "Document Information"
    **Standard ID**: ATL-STD-XX-TP-GN-001 
    **Version**: 1.0  
    **Last Updated**: 2026-01-30  
    **Status**: Active

    <button class="print-button" onclick="window.print()" style="margin-top:10px;">🖨️ Print This Template</button>


## 1 Table of Contents
{{ toc }}
---

## 2 Purpose
The BIM Execution Plan (BEP) details how the BIM Group, Design Division, and Consultants will collaborate for effective BIM use. It specifies processes for information exchange, coordination, and collaborative design, while highlighting BIM’s value in data reuse throughout the project lifecycle. The BEP clarifies workflows for compliance and consistent digital delivery, ensuring reliable BIM data during each Stage. 

__Refer to the ATL BIM Standard for unaddressed issues; this BEP notes any project-specific changes.__

## 3 Project Overview

|Project Information        |           |
|---------------------|-----------------|
| Project Title       | [Insert here]   |
| Client              | [Insert here]   |
| Location            | Atlanta, Georgia|
| Project Description | [Insert here]   |
| Project Phase       | [Insert here]   |
| Project Number      | [Insert here]   |

## 4 BIM Objectives and Uses

- Design Authoring (Revit)
- Coordination & Clash Detection (Navisworks, ACC Coordination)
- 4D Sequencing (Navisworks Timeliner)
- Quantity Takeoffs (Revit, Navisworks Quantification)
- Facilities Management (Tandem)

## 5 Project Team & Stakeholders

__ATL-Team__

|Name|Company|Role|Email|
|----|-------|----|-----|
|Jane Bimmer|Arch Company A|BIM Manager|JB@archA.com|
|....|

Consultant-Team

|Name|Company|Role|Email|
|----|-------|----|-----|
|...|

## 6 Roles and Responsibilities

- BIM Manager: Oversees all modeling standards, clash detection, ACC structure
- BIM Coordinators: Per discipline, responsible for weekly model updates
- Model Authors: Responsible for geometry and data
- ACC Admin: Controls user access, folder structure, permissions

## 7 BIM Scope

- Model Authoring Software: Autodesk Suite
- Coordination Software: Navisworks Manage, BIM Collaborate
- LOD/LOI: Based on the [Information Delivery Plan](docs\template-docs\tp-gn-002.md)
- Model Discipline Breakdown: 

List of all the disciplines to be filled in this table:

|Discipline|File Name|Description|
|----------|---------|-----------|
*Architecture*|*F1021014-ATL-XX-M3-A-01.rvt*|*Existing Conditions*|

## 8 Deliverables Milestones

|STEPS|DESCRIPTION|DATE|
|-----|-----------|----|
|Mobilization & Definition|Gather essential resources, establish project goals, timelines, and responsibilities.|TBD|
|Design Kickoff|Coordinate team efforts, share insights, ensure alignment on project objectives.|TBD|
|BIM Kickoff|Address BIM team roles, software requirements, standards, and BIM execution strategy.|TBD|
BIM Execution Plan Submission|Submit and approve the BIM Execution Plan outlining BIM processes, standards, and workflows.|TBD|
|Models Submission for Each Trade|Submit models regularly through ACC platform for coordination and clash detection.|TBD|
|BIM Final Review|Comprehensive assessment of models submitted by each trade through ACC platform.|TBD|
|Final Model Submission for Each Trade|Final coordinated and validated models ready for construction and facility management.|TBD|

## 9 Model Deliverables

- Design Phase: RVT, NWC, PDF, DWG
- Construction Phase: \+4D simulations
- As-Built: LOD 450 Revit models
- Delivery Format: Revit 2025, Navisworks NWC/NWD, IFC where applicable

## 10 Modeling Standards

- File Naming Convention, Revit Templates, Coordinate System, Model Setup, and Object Naming documented in the [Revit Project Setup](docs\standards\dc-gn-003.md) Standard

## 11 Model Exchange and Collaboration

- CDE Platform: Autodesk Construction Cloud (ACC)
- Collaborative Working: _Design Collaboration_ or Standardized ACC hierarchy with permission-based access. Please document how you will achieve collaborative working ensuring all parties have ability to produce work associated with these states:

|Folder/State|Purpose|
|------------|------|
|WIP|Internal workspaces for each discipline/team. Only accessible by authoring team.|
|Shared|Contains information models/data that have been checked and approved for cross-discipline coordination.|
|Published|Final deliverables for construction or handover (e.g., IFC drawings, certified models).|
|Archive|Secure and immutable records of each project phase or milestone by date.|

- Model Sharing Frequency: Weekly uploads for coordination
- Collaboration Platform: BIM Collaborate Pro (live linking with Revit Cloud Worksharing)
- Review Process: ACC Issues tracking, Model Coordination module for clashes. 
- Create a subfolder for each submission in the Published folder:

__Autodesk Construction Cloud (ACC) folder for Milestone Submissions__


|Publish Folder|Submission|Date|
|--------------|----------|----|
|_Name_|_30% Submission_|_01/01/2026_|

## 12 Clash Detection and Coordination

- Clash Software: Navisworks Manage \+ ACC Model Coordination
- Frequency: Monthly
- Tolerance Settings: (e.g., 1/2" MEP, 1" Architectural)
- Clash Assignment Workflow: ACC Issues assigned by BIM Manager to discipline leads
- Tracking: Issues resolved through ACC and logged with reports
- Follow the Standardized color scheme: 

|Discipline|Color|
|----------|-----|
|Architectural|Cyan|
|Electrical|Yellow|
|Electronics|White|
|Vertical Circulation|Orange|
|HVAC|Green|
|Plumbing|Magenta|
|Fire Protection|Red|
|Structural||Blue

## 13 Common Data Environment (ACC)

- CDE Setup:
- - Autodesk Docs for storage
- - Model Coordination for clash
- - Design Collaboration for worksharing
- Folder Permissions: Owner, Design Team, Contractor, Viewer
- Audit Logs & Version Control: Enabled
- Backup Strategy: Daily backup via ACC, version tracking enabled
- Mobile Access: Field tools configured for site use (PlanGrid/Autodesk Build)

## 14 Quality Control / QA

- Model Audit Schedule: Monthly QA review of Revit models
- BIM Model Checklists: (LOD completeness, naming conventions, etc.)
- Navisworks Clash Reports: Distributed weekly
- Design Review Protocol: Based on Design Collaboration Packages in ACC
- Validation Tool Autodesk Doc

