# ATL-STD-XX-DC-GN-005: Civil 3D SOP

!!! info "Document Information"
    **Standard ID**: DC-GN-005  
    **Version**: 0.1  
    **Last Updated**: 2026-11-05  
    **Status**: Draft

---

## 2 INTRODUCTION

### 2.1 Purpose

This Standard Operating Procedure (SOP) sets out a consistent and efficient Autodesk Civil 3D and AutoCAD workflow for the Atlanta Airport, so that civil deliverables come out the same way on every project. It covers roles and responsibilities, project and drawing setup, data management, modeling, plan production, and drawing health.

By applying these practices across all projects, the SOP ensures:

- Predictable and repeatable drawing and model quality.
- Better coordination between civil, airfield, utility, and building disciplines.
- Less rework and fewer production problems.
- Reliable civil data for downstream uses (quantities, as-builts, GIS, and asset management).
- Alignment with the ATL CAD Standards and the ATL BIM Standards.

This SOP is a reference for everyone who authors, references, coordinates, reviews, or delivers Civil 3D and AutoCAD data on ATL projects.

### 2.2 Governing Documents

This SOP puts the following documents into practice. It does not replace them:

| Document | Scope |
|----------|-------|
| ATL Design Standards – Section 8, Computer Aided Drafting (CAD) Standards | Drawing format, sheet size, drawing content, sheet numbering, layering, and file transmittals. |
| [DC-GN-001 Information Structure, Naming, and Format Standard](dc-gn-001.md) | File, sheet, and container naming. |
| [DC-GN-002 P&D BIM Standards](dc-gn-002.md) | Software, Common Data Environment, coordinate system, LOD, and deliverables. |
| [DC-GN-004 Revit SOP](dc-gn-004.md) | Revit setup and coordination with Civil 3D site data. |
| National CAD Standard (NCS), latest edition | Layering, sheet, and file conventions, except where the ATL CAD Standards Appendix B lists an exception. |

If this document conflicts with the BIM Standards or the BIM Naming Convention, the BIM Standards and the BIM Naming Convention take precedence. If this document conflicts with the ATL CAD Standards on drafting matters (sheet format, drawing content, layering, plotting), the ATL CAD Standards take precedence.

!!! note
    Any special condition that requires a change or variance from these procedures needs prior approval from P&D. Submit the request with the **Request for CAD Standards Modification** form (ATL CAD Standards, Appendix A) to the P&D CAD/Mapping Manager. See [Section 13.3](#133-variance-requests).

---

## 3 ROLES AND RESPONSIBILITIES

This section defines the key roles in Civil 3D project delivery and their core responsibilities, so that ownership of data, drawings, and coordination is clear across all teams.

### 3.1 BIM Manager / CAD Manager

**Purpose:**

Leads and oversees all Civil 3D and AutoCAD workflows on a project or program.

**Key Responsibilities:**

- Define, implement, and maintain the Civil 3D template, styles, layer standards, and plot settings for the project.
- Make sure drawings follow the ATL CAD Standards, the naming conventions, the LOD expectations, and the BEP.
- Set up and maintain the project's Data Shortcut project and folder structure in Autodesk Forma (previously known as ACC or Autodesk Construction Cloud).
- Own the project coordinate system set-up and confirm it matches the ATL02 "Airport Grid".
- Approve variances, new styles, and new layers before they are used.
- Act as the main contact for CAD and Civil 3D issues, training needs, and escalations.

### 3.2 BIM / CAD Coordinator

**Purpose:**

Keeps Civil 3D data, references, and drawings aligned within the civil team and with the other disciplines.

**Key Responsibilities:**

- Check that data shortcuts and XREFs resolve correctly and point to the approved Forma locations.
- Coordinate civil data with the Revit Site Model and building disciplines (see [Section 11](#11-coordination-and-clash-detection)).
- Run model health and QA/QC checks before each milestone submittal.
- Track and resolve broken references, duplicate objects, and style or layer drift.
- Prepare and verify eTransmit packages.

### 3.3 Civil Designer / CAD Technician

**Purpose:**

Creates and maintains Civil 3D design objects and plan production drawings that are accurate, coordinated, and compliant.

**Key Responsibilities:**

- Build surfaces, alignments, profiles, corridors, pipe networks, grading, and sections using the approved template and styles.
- Keep each object in its designated source drawing and share it through data shortcuts.
- Keep drawings healthy: purge, audit, and remove incidental work.
- Produce plan, profile, and section sheets that follow the ATL CAD Standards drawing content rules.

**Qualifications:**

- Civil 3D and Autodesk Forma (with Desktop Connector) proficiency.
- Working knowledge of data shortcuts, XREFs, and the Sheet Set Manager.
- Familiarity with the ATL CAD Standards, the NCS layering guidelines, and the ATL02 coordinate system.

### 3.4 Engineers of Record (Civil, Airfield, Drainage, Utilities)

**Purpose:**

Makes sure that engineering intent, design criteria, and analysis results are correctly represented in the Civil 3D model.

**Key Responsibilities:**

- Define the design criteria (for example FAA Advisory Circulars for airfield work, GDOT and AASHTO for roadways, and the City of Atlanta Department of Watershed Management requirements for stormwater and utilities).
- Check that alignments, profiles, grades, pipe sizes, and inverts meet those criteria.
- Review hydraulic and hydrologic analysis results that come from, or feed into, the Civil 3D model.
- Seal the final drawings when required (see [Section 7.5](#75-submittal-milestones-revisions-and-as-builts)).

### 3.5 Surveyor

**Purpose:**

Provides the existing conditions data that the design is built on.

**Key Responsibilities:**

- Deliver survey data in the ATL02 "Airport Grid" coordinate system and the project vertical datum, with the control used documented.
- Deliver points, breaklines, and an existing ground surface in native Civil 3D format, plus a survey report and metadata.
- Use the agreed point description codes so that description keys and figure prefixes work correctly.

### 3.6 Project Team Members Using Civil 3D / AutoCAD (General Contributors)

**Purpose:**

Supports project delivery through consistent, responsible use of Civil 3D and AutoCAD.

**Key Responsibilities:**

- Follow all approved CAD and Civil 3D standards, including templates, styles, layers, and file handling rules.
- Work only in Autodesk Forma through Desktop Connector, never from local copies.
- Reference other teams' data through data shortcuts and XREFs. Never copy, explode, or bind it.
- Ask the BIM/CAD Coordinator or the BIM Manager for help when procedural or technical issues come up.

> **"If responsibilities aren't clear, quality collapses."**

---

## 4 PROJECT SETUP

This procedure defines how project teams set up the software, the Forma folders, the Data Shortcut project, and the drawing template, so that every Civil 3D drawing starts the same way.

### 4.1 Pre-Requisites

- **Software/Services:** Use the approved Civil 3D, AutoCAD, and Desktop Connector versions for the program.

!!! note
    P&D only accepts submittals prepared with Autodesk products, in native, fully functional, editable formats that DOA can use in the AutoCAD environment. Drawings created in other software and translated to DWG are **not** accepted. Civil 3D objects are not backward compatible: a drawing saved in a newer Civil 3D release cannot be opened as Civil 3D objects in an older one. All team members must use the same release before starting work.

| Software | Version |
|----------|---------|
| Autodesk Civil 3D 2026 | Latest update approved by P&D (confirm with the BIM Team) |
| Autodesk AutoCAD 2026 | Latest update approved by P&D (confirm with the BIM Team) |
| Desktop Connector | 17.1.0.16 |

- **Access:** Confirm access to the project's Autodesk Forma site and to the Standards/Templates folders.
- **CAD Standard Link:** At contract award, P&D provides a CAD Standard Link containing:
    - Cover sheet example.
    - ATL base map XREF.
    - Base street names XREF.
    - Airport grid ticks XREFs (for several scales).
    - Title block border sheet.
    - DOA plot style (`.ctb`) files.
- **Standards:** Review the [BIM Standards](dc-gn-002.md) and the ATL CAD Standards before starting work.
- **Plugins:** Teams may use plugins, add-ins, scripts, and Dynamo for Civil 3D at their own risk. Final drawings must not depend on a third-party object enabler to display or edit correctly.

### 4.2 Autodesk Forma Folder Structure

All active Civil 3D and AutoCAD files stay in the project's Autodesk Forma site and are accessed through Desktop Connector. The Civil 3D folder structure sits within the WIP / Shared / Published / Archive areas defined in [DC-GN-002 Section 5.2](dc-gn-002.md#52-folder-structure).

!!! note
    **No active project files should be saved locally.** Local copies break data shortcut and XREF paths for everyone else on the team.

**Recommended structure inside the civil WIP folder:**

```text
WIP/
└── CV/                                  ← Civil 3D Working Folder (set in Civil 3D)
    └── <WBS>_C3D/                       ← Data Shortcut Project Folder
        ├── _Shortcuts/                  ← Created and managed by Civil 3D. Do not edit.
        ├── 01_Survey/                   ← Survey points, figures, existing ground
        ├── 02_Reference/                ← ATL base map, grid ticks, other-discipline XREFs
        ├── 03_Surfaces/                 ← Design and datum surfaces
        ├── 04_Alignments/               ← Alignments and profiles
        ├── 05_Corridors/                ← Corridors and assemblies
        ├── 06_Grading/                  ← Feature lines and grading
        ├── 07_PipeNetworks/             ← Storm, sanitary, water, and pressure networks
        ├── 08_Sections/                 ← Sample lines and cross sections
        └── 09_Sheets/                   ← Plan production (sheet) drawings and sheet set (.dst)
```

!!! note
    Folder names may be adjusted per project with BIM Manager approval, but the split between **source drawings** (folders 01–08) and **sheet drawings** (folder 09) must be kept.

### 4.3 Using the Civil 3D Template (Mandatory)

The Civil 3D template (`.dwt`) carries the units, coordinate system, NCS layers, object and label styles, description keys, plot styles, and page setups. Starting from the template is the only reliable way to make drawings consistent.

!!! note
    Where P&D provides an ATL Civil 3D template, it must be used. Where it does not, the consultant's template must be set up to meet this SOP and the ATL CAD Standards, and submitted to the BIM Team for review at the BIM Kickoff Meeting.

#### 4.3.1 Procedure – Create a Drawing from the Template

1. In Civil 3D, select **New** and browse to the approved template in the Standards/Templates folder.
2. Open **Toolspace > Settings > Drawing Settings** and confirm:
    - **Units and Zone:** drawing units are decimal **feet** (one drawing unit equals one foot) and the zone is the ATL02 "Airport Grid" provided with the template or base map. Do not reassign or transform the coordinate system.
    - **Object Layers:** object layers follow the NCS layer names in the template.
    - **Abbreviations and Ambient Settings:** stationing, elevation, and precision formats match the template.
3. Confirm that the title block is in **paper space**, the page setups use the ARCH E1 and ANSI B (Modified) sizes, and the DOA `.ctb` plot style is assigned (see [Section 10](#10-plan-production-and-sheet-standards)).
4. Save the drawing to the correct Forma folder using the [DC-GN-001](dc-gn-001.md) naming convention (see [Section 13](#13-file-naming-convention)).

!!! warning
    Never start a production drawing from **acad.dwt**, a blank drawing, or a copy of another project's drawing. Doing so brings in foreign styles, layers, and coordinate settings that are hard to remove later.

### 4.4 Data Shortcut Project Setup

Data shortcuts let one source drawing own each Civil 3D object while other drawings reference it read-only. This is the standard way to share Civil 3D data on ATL projects.

#### 4.4.1 Procedure – Set the Working Folder and Create the Data Shortcut Project

1. In **Toolspace > Prospector**, right-click **Data Shortcuts** and select **Set Working Folder**. Browse to the civil WIP folder through Desktop Connector (for example `Autodesk Docs > <Project> > WIP > CV`).
2. Right-click **Data Shortcuts** and select **New Data Shortcuts Project Folder**. Name it `<WBS>_C3D` and, if available, use the ATL project folder template to create the subfolders in [Section 4.2](#42-autodesk-forma-folder-structure).
3. Confirm that **Data Shortcuts** in Prospector shows the new project as the current project.
4. Tell the team the Working Folder and project name so everyone points to the same location.

#### 4.4.2 Data Shortcut Rules

- Each Civil 3D object has **one** source drawing and **one** owner.
- Create shortcuts from the source drawing with **Create Data Shortcuts**. Reference them into other drawings with **Create Reference**.
- Do **not** promote data references to edit them. If a change is needed, ask the owner of the source drawing.
- After the source drawing is saved, use **Synchronize** in the referencing drawings and review the changes before plotting.
- Repair broken references with **Data Shortcuts > Validate Data Shortcuts** and the **Data Shortcuts Editor**. Do not recreate the object.
- Do not rename or move source drawings without the BIM/CAD Coordinator. Doing so breaks every shortcut that points to them.

---

## 5 DRAWING SETUP

### 5.1 Drawing Breakdown Structure

Civil 3D performance and teamwork depend on keeping drawings small and single-purpose. Separate the project into source drawings by object type and area, and assemble them in sheet drawings through data shortcuts and XREFs.

| Drawing | Contents | Shared By |
|---------|----------|-----------|
| Survey | Survey points, point groups, figures, existing ground surface | Data shortcut (surface), XREF (linework) |
| Base / Existing Conditions | ATL base map, existing utilities, property lines, existing features | XREF |
| Surfaces | Design surfaces, datum and comparison surfaces | Data shortcut |
| Alignments & Profiles | Horizontal alignments, profiles | Data shortcut |
| Corridors | Corridors, assemblies, corridor surfaces | Data shortcut (surfaces, alignments) |
| Grading | Feature lines, grading groups, pond and pad grading | Data shortcut (surfaces) |
| Pipe Networks | Gravity and pressure networks (one network type per drawing when large) | Data shortcut |
| Sections | Sample line groups, section views, quantity takeoff | Data shortcut |
| Sheets | View frames, sheet layouts, title blocks, annotation | Not shared |

!!! note
    Only **one copy** of each base file may be used throughout the contract. Share base files by **XREF**, never by **INSERT** or copy and paste.

### 5.2 Coordinate System and Geolocation

All Civil 3D drawings must be set up in the Atlanta Airport's official coordinate system, the ATL02 "Airport Grid", as required by [DC-GN-002 Section 7](dc-gn-002.md#7-coordinate-systems). This is the default coordinate system named in the ATL CAD Standards.

!!! note
    Each team **must** check the coordinates, rotation, and elevation datum when a new drawing is set up. The Civil 3D drawings and the Revit Site Model must share the same origin so that the building models line up with the civil design.

**Steps to check geolocation:**

1. XREF the ATL base map and the airport grid ticks from the CAD Standard Link at **0,0,0**, with a scale of **1** and a rotation of **0**. Use **Overlay** as the reference type.
2. Check that known survey control points and grid tick intersections match their published ATL02 coordinates.
3. Check that the elevations of control points match the project vertical datum given in the survey report.
4. Record the check (control point IDs, published vs. measured values) in the project's QA/QC log.
5. Before modeling starts, coordinate with the Revit team to confirm that the Revit Site Model lines up with the Civil 3D base map (see [DC-GN-004 Section 5.3](dc-gn-004.md#53-linking-in-a-site-model-acquiring-coordinates)).

!!! warning
    Never move, rotate, or scale civil data to "fit" a reference. If something does not line up, stop and tell the BIM/CAD Coordinator. The problem is in the reference or the survey, and it must be fixed at its source.

### 5.3 Drawing Units and Scale

- Draw all entities at full size (**1:1**) in **model space**.
- Engineering drawings use decimal units with **one drawing unit equal to one foot**.
- Set the annotation scale per viewport. Use annotative styles from the template rather than separate text sizes for each scale.
- 2D entities that do not represent 3D design data (annotation, title block items, linework from the base map) must have a **Z value of 0**. Civil 3D objects that carry elevations by design (surfaces, feature lines, corridors, pipe networks, 3D polylines) keep their true elevations.

### 5.4 External References (XREFs)

- Attach all XREFs as **Overlay**, with **relative** paths, at 0,0,0, scale 1, and rotation 0.
- Load XREFs only from the approved Forma folders. Never reference a local or emailed copy.
- Do **not** bind or insert XREFs into the base drawings.
- Do not nest XREFs more than one level deep.
- Use **Clip** and **Layer** controls to manage what is shown. Do not edit the referenced file to suit one sheet.

### 5.5 Survey Data

Existing conditions data is the base for the whole design and must be traceable.

**Procedure to import survey data:**

1. Create the survey drawing from the template.
2. Import points with **Import Points** using the agreed file format (for example PNEZD, comma delimited). Check the coordinate and elevation of at least three control points after import.
3. Apply the template's **description key set** so that points land on the correct layers with the correct styles and labels.
4. Organize points into **point groups** (for example Control, Topo, Utilities, Trees). Do not delete the `_All Points` group.
5. Process figures (linework) using the agreed figure prefix database, and use them as breaklines where appropriate.
6. Build the existing ground surface (see [Section 6.1](#61-surfaces)).
7. Record the survey source, date, control, and datum in the drawing's **Drawing Properties** and in the surface description.

!!! note
    Survey data received from P&D or from others is reference information. Consultants and contractors must get their own survey of the project areas and check the information before detailed design (see [DC-GN-002 Section 10.2](dc-gn-002.md#102-site-model-sm)).

### 5.6 Object Naming Convention

Consistent object names make data shortcuts, sheets, and reviews easy to read. Use the naming patterns below unless the BEP defines others.

| Object | Pattern | Example |
|--------|---------|---------|
| Surface – existing | `EG_<Source>_<YYYYMMDD>` | `EG_Survey_20261015` |
| Surface – design | `FG_<Area/Element>` | `FG_TWY-B` |
| Surface – datum / subgrade | `DT_<Area/Element>` | `DT_TWY-B_Subgrade` |
| Surface – volume | `VOL_<Base>_vs_<Compare>` | `VOL_EG_vs_FG_TWY-B` |
| Alignment | `<Element>_<Descriptor>` | `TWY-B_CL`, `RD-Loop_CL` |
| Profile – existing | `<Alignment>_EG` | `TWY-B_CL_EG` |
| Profile – design | `<Alignment>_FG` | `TWY-B_CL_FG` |
| Corridor | `COR_<Element>` | `COR_TWY-B` |
| Pipe network | `<System>_<Area>` | `STM_TWY-B`, `SAN_Bldg100` |
| Structure | `<Type>-<Number>` | `CB-101`, `MH-205` |
| Pipe | `<System>-<From>-<To>` | `STM-CB101-MH205` |
| Sample line group | `SLG_<Alignment>` | `SLG_TWY-B_CL` |

!!! note
    Use the **Name Templates** in the object and feature settings so that Civil 3D fills in these names automatically. Do not leave default names such as `Surface1` or `Alignment - (1)` in submitted drawings.

---

## 6 MODELING STANDARDS

### 6.1 Surfaces

**Why:** Surfaces drive profiles, corridors, grading, pipe cover, quantities, and the Revit toposolid. An unreliable surface makes everything downstream unreliable.

**Rules:**

- Build surfaces from their source data (points, breaklines, contours, boundaries) through the **surface definition**. Do not paste one surface into another unless you intend to combine them, and document it in the surface description.
- Add an **outer boundary** to every surface to remove false triangles at the edges.
- Use **breaklines** for edges of pavement, curbs, ridges, ditches, and walls.
- Avoid manual triangle edits (**Delete Line**, **Swap Edge**). If they are needed, keep them few and record them in the surface description.
- Use a simplified or decimated copy for very large surfaces (for example LiDAR) and keep the full-density source in its own drawing.
- Turn on **Rebuild – Automatic** only while editing. Turn it off in source drawings that are referenced by many sheets.
- Use the template surface styles for contour intervals (for example 1 ft minor and 5 ft major for design sheets, unless the project requires otherwise).

!!! warning
    Never explode a surface or convert it to polylines and 3D faces to "lock" it. Exploded surfaces cannot be checked, updated, or used by other disciplines.

### 6.2 Alignments and Profiles

- Create alignments with the **Alignment Creation Tools** using design criteria files and checks (for example FAA Advisory Circular design criteria for runways and taxiways, and GDOT/AASHTO for roadways).
- Stationing must follow the project **baseline direction**. The sheet sequence follows the same direction (see [Section 10.3](#103-drawing-content)).
- Use the template's alignment and profile label sets for stations, geometry points, and curve data.
- Check that alignments have no design criteria violations before each submittal. If a violation is intentional, the Engineer of Record documents it.
- Create existing ground profiles from the referenced surface. Do not draw them as polylines.
- Keep the profile view style, band set, and vertical exaggeration the same for the same sheet type throughout the project.

### 6.3 Corridors and Assemblies

- Build assemblies from approved subassemblies (stock Civil 3D or Subassembly Composer `.pkt` files approved by the BIM Manager). Store custom `.pkt` files in the project Standards folder.
- Name assemblies by element and typical section (for example `ASM_TWY-B_Typ-01`).
- Split long or complex corridors into **regions** and, where needed, into separate corridors by element or phase.
- Use frequencies that match the design intent. Avoid very small frequencies that make the drawing heavy without improving accuracy.
- Set targets (widths, offsets, elevations) explicitly. Do not use fixed offsets where a target is intended.
- Rebuild the corridor and resolve all **Corridor Properties > Event Viewer** errors before sharing.
- Extract corridor surfaces (top, datum) and share them by data shortcut.

### 6.4 Grading and Feature Lines

- Use **feature lines** for pads, ponds, and site grading. Keep each grading area in its own **site** to avoid unwanted interaction between feature lines.
- Use grading groups only where they add value. Large grading groups slow drawings down, so prefer feature line and surface workflows where practical.
- Check slopes with surface **slope analysis** and **elevation analysis** before submittal.

### 6.5 Pipe Networks

- Use the template **parts lists** for each system (storm, sanitary, water, and so on). Do not add parts from another project's catalog without BIM Manager approval.
- Use the template **rules** for cover, slope, and drop across structures, and check results against the design criteria.
- Pipe and structure labels must show the data needed for the drawings (size, material, slope, inverts, rim elevations).
- Reference the design surface for rim and cover calculations, and update the reference when the surface changes.
- Run **Interference Check** between networks (see [Section 11](#11-coordination-and-clash-detection)).
- If a hydraulic analysis is done in Storm and Sanitary Analysis or another approved tool, keep the analysis file with the source drawing and make sure the Civil 3D network matches the analyzed network.

### 6.6 Sections and Quantities

- Create sample lines along each design alignment at the stations required by the drawings and quantity takeoff.
- Use the template section view styles and group plot styles for cross section sheets.
- Use **Compute Materials** (earthwork and corridor materials) with a defined **Quantity Takeoff Criteria** for cut and fill. Record the criteria and shrink/swell factors used.
- Check earthwork results against a surface-to-surface volume (TIN volume surface) as an independent check.

### 6.7 Styles, Layers, and Object Properties

- Use only the object, label, and table styles in the approved template. New styles need BIM Manager approval and must be added to the template, not created in individual drawings.
- Use only **NCS layer names** (see [Section 9.2](#92-layering)).
- Set color, linetype, and lineweight **ByLayer**. Do not override properties per object.
- Do not use **Explode** on Civil 3D objects, blocks, or XREFs.
- Use **Export to AutoCAD** (`EXPORTTOAUTOCAD`) only to produce a separate exchange copy for parties without Civil 3D. Never use it on a working or submitted source drawing.

### 6.8 Drawing Performance Rules

Drawings must stay light and responsive throughout the project.

**Best Practices:**

- Keep each drawing to one purpose and one area (see [Section 5.1](#51-drawing-breakdown-structure)).
- Purge and audit regularly (for example weekly and before every milestone). See [Section 12](#12-drawing-health-qaqc).
- Detach unused XREFs and images. Unload XREFs that are not needed in the current task.
- Turn off automatic rebuild on surfaces and corridors in drawings that are not being edited.
- Delete all incidental work (construction lines, test objects, unused layouts) before sharing.

---

## 7 DELIVERABLES AND EXPORTS

### 7.1 Quality Assurance for Deliverables

Before any milestone submittal, every drawing in the package must pass the QA/QC checklist in [Section 12.2](#122-submittal-qaqc-checklist). The BIM/CAD Coordinator signs off on the checklist before the package is transmitted.

### 7.2 Required File Formats

For each milestone set out in the BEP, submit the following (see also [DC-GN-002 Section 11](dc-gn-002.md#11-deliverables)):

| Format | Description | Required |
|--------|-------------|----------|
| DWG | Native, fully editable Civil 3D and AutoCAD drawings (source and sheet drawings) | Always |
| ZIP | eTransmit package of all drawings and their dependencies (see [Section 7.3](#73-etransmit-file-transmittal)) | Always |
| PDF | Multi-sheet PDF of the full set, plus a PDF of each individual sheet | Always |
| NWC | Navisworks cache files for coordination (see [Section 7.4](#74-exporting-nwcs-landxml-and-ifc)) | When required by the BEP |
| XML | LandXML of surfaces, alignments, and pipe networks | When required by the BEP |
| IFC | IFC export of civil objects | When required by the BEP |
| Supporting data | Survey files, point files, analysis files, Excel/CSV, images, and any other data needed to reproduce the drawings | Always |

### 7.3 eTransmit (File Transmittal)

Each submittal must be transmitted as a zipped **eTransmit** package so that every drawing and every element it depends on is captured.

**Procedure:**

1. Prepare the drawings.
    - Make sure all team members have saved and closed the drawings.
    - Synchronize all data references and reload all XREFs.
    - **Purge** (several passes, including regapps) and **Audit** each drawing, fixing errors.
    - Zoom each drawing to extents and lock all viewports.
    - Save each drawing.
2. Run eTransmit.
    - Open the sheet set (`.dst`) or the main sheet drawing and launch **eTransmit**.
    - Check that all XREFs, data shortcut source drawings, images, fonts, and plot styles are listed.
    - Set the transmittal package type to **Zipped (\*.zip)**.
    - Set the file format to the current P&D release (keep existing file format).
    - Use **one root project folder** (keep the files and folders together).
    - Include: **fonts**, **textures from materials**, **files from data links**, **photometric web files**, and **sheet set data and files**.
    - Include the **Data Shortcut** project files (`_Shortcuts` folder) and their source drawings.
3. Check the eTransmit output.
    - Unzip the package to an empty folder and open the sheet drawings.
    - Check that all XREFs and data references resolve inside the package, and that no files are missing.
4. Deliver the package.
    - Upload the package and the PDFs to the assigned Autodesk Forma site.
    - Create a transmittal stating which files are for review and which are for reference only (see [DC-GN-002 Section 11.2](dc-gn-002.md#112-autodesk-forma-model-transmittal-process)).
    - Label the submittal with the submitter's name, project title, WBS number, issued-for date, issued-for stage, and contract number.

### 7.4 Exporting NWCs, LandXML, and IFC

- **NWC:** Use `NWCOUT` from a coordination drawing that contains only the objects needed (design surfaces, corridors, pipe networks, structures) as data references. Export in the ATL02 coordinates. Do not move objects to the origin.
- **LandXML:** Use **Export to LandXML** for surfaces, alignments, profiles, and pipe networks when other software needs the data. Check units and coordinates in the exported file.
- **IFC:** Use the Civil 3D IFC export when the BEP requires it, and check it in a viewer before submittal.
- **Revit:** Share design surfaces with the Revit team from the Forma-hosted source drawing (for example with Revit **Link Topography** or an approved toposolid workflow). Agree on the method at the BIM Kickoff Meeting.

### 7.5 Submittal Milestones, Revisions, and As-Builts

- Follow the design review phases in [DC-GN-002 Section 11.1](dc-gn-002.md#111-project-submittals): Schematic Design (30%), Design Development (60%), Construction Documents (90%), and Issue for Construction (100%).
- Additional submittals or resubmittals may be required at any design phase, as scheduled in the DOA Task Order.
- **Revision clouds are not used** to show additions or changes during the design phases. Changes during the bid phase are made by **addenda**.
- Drawings **Issued for Permit** and drawings **Released for Construction** are identical, except that Issued for Permit drawings are signed and sealed by the registered professional approving their release.
- **As-Builts** must be finished in Civil 3D/AutoCAD and clearly marked **"As-Built"**. Submit a complete set in both hard copy and electronic form.

---

## 8 LEVEL OF DEVELOPMENT (LOD)

All civil models must meet the LOD requirements in the project's BIM Execution Plan (BEP). Please refer to the [BIM Standards](dc-gn-002.md#81-level-of-development-lod) for the LOD definitions and the specific requirements for each submission.

**Requirements:**

| Discipline | Construction Start | As-Built |
|------------|-------------------|----------|
| Civil | LOD 300 | LOD 350 |

**Process to reach LOD 300:**

- **Schematic Design (30%):** Existing ground surface, preliminary alignments and profiles, conceptual grading, and main utility routes.
- **Design Development (60%):** Design alignments and profiles meeting design criteria, corridors for main elements, preliminary pipe networks with sizes, and preliminary earthwork.
- **Construction Documents (90%):** Final corridors and grading surfaces, pipe networks with final sizes, inverts, and structures, cross sections, and quantities.
- **As-Built:** Surfaces, utilities, and structures updated to field-verified locations and elevations.

**Do:**

- Model all civil elements to the required LOD before each milestone.
- Make sure grades, inverts, and utility crossings are coordinated by LOD 300.
- Update both geometry and data to field-verified conditions for the As-Built submittal.

**Don't:**

- Don't submit drawings with placeholder or schematic geometry at the construction stage.
- Don't represent 3D design data (grades, inverts, surfaces) with 2D linework only.
- Don't leave required object data (pipe material, size, structure type) empty.

---

## 9 DATA, LAYERING, AND STANDARDS COMPLIANCE

### 9.1 Object Data

- Fill in object descriptions for surfaces, alignments, corridors, and pipe networks (source, date, purpose).
- Use **Property Sets** for asset data when the project's Information Delivery Plan (IDP) requires it (see [DC-GN-002 Section 8](dc-gn-002.md#8-information-delivery-plan-idp)).
- Keep pipe and structure part data (material, size, type) accurate, because it feeds quantities, as-builts, and asset management.

### 9.2 Layering

Follow the National CAD Standards (NCS), latest edition, Layering Guidelines, with the exceptions in the ATL CAD Standards Appendix B.

- Use **only NCS layer names**. Any other layer needs DOA P&D approval.
- Use the **minimum number of layers** needed to separate entities. Do not create extra, redundant, or overly detailed layers.
- Use the layer **color, linetype, and lineweight** set out by the NCS.
- **Purge unused layers** before submittal, so the drawing holds only the layers needed to display and plot its content. This makes later prints match the original.
- Use the **DOA `.ctb`** files to plot.

**ATL layer name structure (ATL CAD Standards Appendix B):**

| Field | Content | Description |
|-------|---------|-------------|
| Field 1 | Discipline Code | Discipline designator (for example `C` Civil, `V` Survey/Mapping, `L` Landscape). |
| Field 2 | Status | Status of the work (for example `N` New, `E` Existing, `D` Demolish, `F` Future, `T` Temporary). |
| Field 3 | Major Group | Building system or element type (for example `TOPO`, `ROAD`, `STRM`, `SSWR`, `WATR`). |
| Field 4 | Minor Group | Further breakdown of the major group (for example `MAJR`, `MINR`, `CNTR`, `PIPE`). |

!!! note
    Civil 3D object layers are set in **Drawing Settings > Object Layers** and in the styles. Make sure these settings use NCS names so that new objects never land on layer `0` or on default Civil 3D layer names.

### 9.3 Standards Checking

- Attach the ATL drawing standards file (`.dws`) to each drawing with **Configure Standards** where one is provided, and run **Check Standards** before every submittal.
- Use the Civil 3D **Import Styles and Settings** (from the template) to bring drawings back in line with the template instead of fixing styles one by one.

---

## 10 PLAN PRODUCTION AND SHEET STANDARDS

### 10.1 Sheet Size and Format

The P&D standard engineering drawing size is **ARCH E1 (30" x 42")** for full-size sheets. **ANSI B (Modified)** is used for half-size sheets. Other sizes need prior approval from the P&D Project Manager. All sheets issued as one set must be the same size.

| Size Designation | Vertical | Horizontal | Top and Bottom Margin | Left Margin | Right Margin |
|------------------|----------|------------|-----------------------|-------------|--------------|
| ARCH E1 | 30" | 42" | 1/2" | 1-1/2" | 1/2" |
| ANSI B (Modified) | 15" | 21" | 1/4" | 3/4" | 1/4" |

- Place all title blocks in **paper space**, using the title block border from the CAD Standard Link.
- **Lock all viewports.**
- Use the P&D title sheets and contract borders for every submitted sheet.

### 10.2 Plan Production Workflow

1. Create **view frames** along the alignment with **Create View Frames**, using the template's plan and plan-profile layouts.
2. Create sheets with **Create Sheets**, adding them to the project **Sheet Set** (`.dst`) in the `09_Sheets` folder.
3. Number and name sheets per [Section 10.4](#104-sheet-numbering-and-naming).
4. Fill in title block fields through **sheet set** properties and fields, not as plain text.
5. Check each sheet for the required drawing content (see [Section 10.3](#103-drawing-content)).

### 10.3 Drawing Content

All plan sheets provided to P&D must include and follow these rules (ATL CAD Standards Section 3.0):

- A **scale bar** on all site plans.
- A **north arrow** always oriented to the bottom right of the page or rotated clockwise.
- The **same north arrow direction** on all plan sheets.
- **Airport coordinate grid ticks at 5" spacing** covering the whole project area on all civil site plans. Use the grid ticks XREF for the sheet's scale from the CAD Standard Link.
- The drawing sequence follows the **baseline direction** (where applicable).
- Details provided by other agencies are shown on **separate sheets**.

### 10.4 Sheet Numbering and Naming

Sheet numbers and names follow the NCS, with the DOA exceptions in the ATL CAD Standards Appendix B. These are reproduced in [DC-GN-001 Section 3.11 Sheet Naming Convention](dc-gn-001.md#311-sheet-naming-convention).

Every sheet number is made up of the **discipline prefix**, the **group code number**, and the **drawing sequence** (for example `C 8.1.1`). New sheets added after the release-for-bid set use the last number in the sequence (for example `C 8.1.1`, `C 8.1.2` (new sheet), `C 8.2.1`).

**Civil (C) Series:**

| Drawing Number | Description |
|----------------|-------------|
| C 0.1.1 | Summary of Quantities |
| C 1.1.1 | Legend, Abbreviations, General Notes, and Key Map |
| C 2.1.1 | Construction Control Plan and Notes |
| C 3.1.1 | Project Phasing |
| C 4.1.1 | Traffic Control Plans and Details |
| C 5.1.1 | Typical Sections |
| C 6.1.1 | Existing Conditions |
| C 7.1.1 | Demolition Plan |
| C 8.1.1 | Site Plan (Profile may be on this sheet) |
| C 9.1.1 | Geometric Control Plan (Including Curve Tables) |
| C 10.1.1 | Runway, Taxiway or Roadway Profiles |
| C 11.1.1 | Super Elevation Plans or Tables |
| C 12.1.1 | Paving and Joint Plans |
| C 13.1.1 | Paving and Joint Details |
| C 14.1.1 | Grading, Drainage, and Utility Plans (Underdrain may show here) |
| C 15.1.1 | Detailed Pavement Grades |
| C 16.1.1 | Grading, Drainage, and Utility Details |
| C 17.1.1 | Drainage and Utility Profiles |
| C 18.1.1 | Surface Settlement Platform Layout |
| C 19.1.1 | Surface Settlement Platform Details |
| C 20.1.1 | Underdrain Plans |
| C 21.1.1 | Underdrain Details |
| C 22.1.1 | Striping and Signage Plans |
| C 23.1.1 | Striping and Signage Details |
| C 24.1.1 | Fencing Plans |
| C 25.1.1 | Fencing Details |
| C 26.1.1 | Miscellaneous Details |
| C 27.1.1 | Erosion Control Plans and Details |
| C 28.1.1 | Boring Location Plan |
| C 29.1.1 | Cross Sections |
| C 30.1.1 | Traffic Signal Plans |

!!! note
    Airfield electrical (EA), landscape (L), and other discipline series are listed in [DC-GN-001 Section 3.11.1](dc-gn-001.md#3111-drawing-types). Special sheets may be created or combined only with an approved Request for CAD Standards Modification.

---

## 11 COORDINATION AND CLASH DETECTION

Civil data must be coordinated with the airfield, building, and utility disciplines throughout design. Follow the coordination meetings and clash detection process in [DC-GN-002 Sections 9 and 10.7](dc-gn-002.md#9-project-coordiantion-meetings).

**Process to perform a utility interference check in Civil 3D:**

1. Reference all pipe networks to be checked into one coordination drawing through data shortcuts.
2. Select **Analyze > Interference Check** and choose the networks.
3. Set the 3D proximity criteria to the minimum required separation.
4. Review each interference and resolve it in the source drawing.
5. Synchronize the references and run the check again until no unresolved interferences remain.

**Process to coordinate with other disciplines:**

1. Export the coordination drawing to NWC (see [Section 7.4](#74-exporting-nwcs-landxml-and-ifc)).
2. Upload the NWC to the Shared folder in Autodesk Forma.
3. The BIM Coordinator federates it with the discipline models in Navisworks or Forma Model Coordination and runs the clash tests.
4. Resolve assigned clashes in the Civil 3D source drawings and reissue the NWC.

---

## 12 DRAWING HEALTH & QA/QC

### 12.1 Drawing Health Routine

Run this routine weekly and before every milestone submittal:

| Command | Purpose |
|---------|---------|
| `AUDIT` (Fix errors = Yes) | Finds and fixes database errors. |
| `PURGE` (all items, several passes) | Removes unused layers, blocks, styles, and linetypes. |
| `-PURGE` > `Regapps` | Removes registered applications brought in by foreign drawings. |
| `-PURGE` > `Zero-length geometry` / `Empty text objects` | Removes zero-length and empty objects. |
| `OVERKILL` | Removes duplicate and overlapping linework (2D linework only). |
| `RECOVER` | Use when a drawing will not open or `AUDIT` cannot fix it. |
| Data Shortcuts > Validate | Confirms all data references resolve. |
| `XREF` palette | Confirms all XREFs are loaded, relative, and from the approved folders. |
| `CHECKSTANDARDS` | Confirms layers, styles, and linetypes match the standard. |

!!! warning
    Purging Civil 3D styles from source drawings can remove styles that sheet drawings need. Purge styles in source drawings only after checking that the template can restore them.

### 12.2 Submittal QA/QC Checklist

- [ ] Drawing was created from the approved template and uses the current P&D release.
- [ ] Drawing is saved in the correct Forma folder with a [DC-GN-001](dc-gn-001.md) file name.
- [ ] Coordinate system is ATL02 "Airport Grid", checked against control points.
- [ ] All entities are 1:1 in model space; 2D entities are at Z = 0.
- [ ] Color, linetype, and lineweight are ByLayer; only NCS layers are used.
- [ ] All XREFs are Overlay, relative, unbound, and loaded from approved folders.
- [ ] All data references resolve and are synchronized.
- [ ] No exploded Civil 3D objects, default object names, or incidental work.
- [ ] Alignments and profiles have no unexplained design criteria violations.
- [ ] Corridors rebuild without errors; pipe network rules pass; interference check is clear.
- [ ] Title block is in paper space; viewports are locked; sheet size is ARCH E1 or ANSI B (Modified).
- [ ] Sheets show scale bar, north arrow, and 5" airport grid ticks as required.
- [ ] Sheet numbers and names follow the DOA sheet numbering system.
- [ ] Drawing has been purged, audited, and zoomed to extents.
- [ ] eTransmit package and PDFs are complete and checked.

---

## 13 FILE NAMING CONVENTION

### 13.1 Drawing Files

All Civil 3D and AutoCAD files follow the [DC-GN-001 File Naming Convention](dc-gn-001.md#3-file-naming-convention):

**WBS – Originator – Level – Type – Role – Number**

| FILE NAME | WHAT IT IS |
|-----------|------------|
| P1234567-ATL-ZZ-SU-CV-001.dwg | Civil survey drawing (points, figures, existing ground) |
| P1234567-ATL-ZZ-M3-CV-001.dwg | Civil 3D source drawing (for example design surfaces) |
| P1234567-ATL-ZZ-M2-CV-001.dwg | 2D reference drawing (for example existing conditions base) |
| P1234567-ATL-ZZ-DR-CV-001.dwg | Civil sheet drawing |

!!! note
    Use the **Number** field to tell source drawings apart, and keep a drawing list in the BEP that maps each number to its content (for example `M3-CV-001` = Surfaces, `M3-CV-002` = Alignments & Profiles, `M3-CV-003` = Corridors).

### 13.2 External Reference Files

The ATL CAD Standards call for XREF file names to begin with an **"X"** (for example `X-Alignment`, `X-E Contours`). On BIM projects hosted in Autodesk Forma, the [DC-GN-001](dc-gn-001.md) file name takes precedence. The reference role of a file is shown by its **Type** code (`M2`/`M3`) and its folder location. Projects that are delivered under the CAD Standards only, outside Forma, may use the "X" prefix if the BEP says so.

### 13.3 Variance Requests

Any proposed variance to sheet numbering, file naming, layering, or other requirements of this SOP or the ATL CAD Standards must be submitted to the P&D CAD/Mapping Manager on the **Request for CAD Standards Modification** form (ATL CAD Standards, Appendix A), describing the suggested change and its benefits. Do not use the variance until it is approved.

---

# Revision Addendum Log

This section outlines the document's history and key events.

| Revision | Date | Description | Author |
|----------|------|-------------|--------|
| Rev 0 | 11/05/2026 | Document Creation | Miguel Henriquez |
| Rev 1 | 11/09/2026 | Changed the Drawing Type Code in the file naming example from D1 to DR to match DC-GN-001. | Miguel Henriquez |
