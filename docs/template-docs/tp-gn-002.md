# ATL-STD-XX-TP-GN-002: Coordination Tracker (Excel)

!!! info "Template Information"
    **Template ID:** ATL-STD-XX-TP-GN-002  
    **Version:** 1.0  
    **File Type:** .xlsx (Excel Workbook)  
    **Excel Version:** 2019+ (Microsoft 365 compatible)  
    **Last Updated:** January 30, 2026

## Overview

The ATL Coordination Tracker is a comprehensive Excel template for managing BIM coordination activities, clash detection, issue tracking, and meeting documentation.

## Download

[:material-download: Download Template](../../downloads/ATL-STD-XX-TP-GN-002.xlsx){ .md-button .md-button--primary }

**File Size:** ~2 MB

## What's Included

### Worksheets

The template contains multiple interconnected worksheets:

#### 1. **Dashboard** (Overview)
- Project summary statistics
- Current clash metrics
- Issue status charts
- Recent activity timeline
- Key performance indicators

#### 2. **Clash Log**
Detailed clash tracking with columns:
- Clash ID
- Date Detected
- Location (Grid/Level)
- Discipline 1 / Discipline 2
- Elements Involved
- Clash Type (Hard/Soft/Clearance)
- Priority (Critical/High/Medium/Low)
- Status
- Assigned To
- Due Date
- Resolution Description
- Date Resolved
- Notes

#### 3. **Issue Tracker**
General coordination issues beyond clashes:
- Issue ID
- Date Raised
- Type
- Description
- Priority
- Owner
- Status
- Resolution
- Closed Date

#### 4. **Meeting Minutes**
Coordination meeting documentation:
- Meeting date and number
- Attendees
- Agenda items
- Discussion notes
- Decisions made
- Action items
- Next meeting date

#### 5. **Action Items**
Tracked tasks from meetings:
- Action ID
- Date Assigned
- Description
- Assigned To
- Due Date
- Status
- Completion Date
- Notes

#### 6. **Model Versions**
Track model submissions for coordination:
- Date
- Week Number
- Discipline
- Model Name
- Version
- File Size
- Changes Summary
- Coordinator Sign-off

#### 7. **Contact List**
Project team directory:
- Name
- Role
- Discipline
- Company
- Email
- Phone
- Responsibility

#### 8. **README**
Instructions and guidelines for using the template

## Features

### Automated Features

✨ **Conditional Formatting:**
- Overdue items highlighted in red
- High priority items in orange
- Completed items in green

✨ **Data Validation:**
- Dropdown lists for consistent data entry
- Status options pre-defined
- Priority levels standardized

✨ **Formulas:**
- Automatic ID generation
- Auto-calculating metrics
- Days overdue calculation
- Status summaries

✨ **Charts:**
- Clash trend over time
- Issues by discipline
- Status distribution
- Priority breakdown

### Pivot Tables

Pre-configured pivot tables for analysis:
- Clashes by discipline pair
- Issues by status and priority
- Resolution time analysis
- Action item tracking

## Usage Instructions

### Initial Setup

1. **Download the template**
   - Save to your project coordination folder
   - **DO NOT** modify the original template

2. **Save with project name**
   ```
   ATL001-BM-ALL-CRD-CoordinationTracker-V01.xlsx
   ```
   (Follow naming standard GN-001)

3. **Fill in project information**
   - Open README tab
   - Update project details on Dashboard
   - Add team members to Contact List

4. **Customize dropdowns (if needed)**
   - Update discipline lists
   - Add project-specific statuses
   - Modify priority levels if required

### Weekly Coordination Workflow

#### Monday: Prepare for Coordination
1. Update **Model Versions** tab with new submissions
2. Review previous week's action items

#### Tuesday: Clash Detection
1. Run clash detection in Navisworks
2. Export clash report
3. Import/enter clashes into **Clash Log** tab
4. Assign priorities and owners

#### Wednesday: Discipline Review
1. Disciplines review assigned clashes
2. Update status to "Reviewed"
3. Add preliminary resolution notes

#### Thursday: Coordination Meeting
1. Use **Meeting Minutes** tab during meeting
2. Discuss critical clashes
3. Record decisions
4. Create action items in **Action Items** tab

#### Friday: Resolution
1. Disciplines update models
2. Update clash status to "Resolved"
3. Add resolution descriptions
4. Prepare for next cycle

### Data Entry Guidelines

#### Clash Log

**Clash ID Format:**
```
C-[YYYY]-[###]
```
Example: `C-2026-001`, `C-2026-002`

**Location Format:**
```
Grid [X]/[Y], Level [Z]
```
Example: `Grid B/3, Level L01`

**Status Options:**
- `New` - Just detected
- `Active` - Assigned for review
- `Reviewed` - Solution identified
- `Resolved` - Fixed in model
- `Approved` - Acceptable as-is
- `Closed` - Verified and closed

#### Issue Tracker

**Issue ID Format:**
```
I-[YYYY]-[###]
```
Example: `I-2026-001`

**Issue Types:**
- Design Coordination
- Model Quality
- Data/Parameter Issue
- Schedule/Sequence
- RFI
- Other

#### Meeting Minutes

**Meeting Numbering:**
```
CCM-[##]
```
Example: `CCM-01`, `CCM-02` (Coordination Meeting)

**Required Information:**
- Date and time
- Attendees (minimum)
- Key decisions
- Action items assigned

## Advanced Features

### Filtering and Sorting

Use Excel's built-in filters to:
- View clashes by discipline
- Filter by priority
- Show only active issues
- Sort by due date

### Reporting

Create custom reports:
1. Use pivot tables for summaries
2. Copy dashboard to PowerPoint
3. Export filtered views to PDF
4. Share weekly status via email

### Integration with Other Tools

**Navisworks Clash Reports:**
- Export clash report from Navisworks as XML or Excel
- Copy relevant data to Clash Log
- Maintain consistent Clash IDs

**Project Management Tools:**
- Export action items for import to MS Project
- Link to issue tracking systems
- Integrate with project schedules

## Customization

### Allowed Modifications

✅ **You can:**
- Add columns for project-specific data
- Create additional charts
- Add new worksheets for project needs
- Modify dropdown values
- Customize conditional formatting colors

### Restricted Modifications

⚠️ **Avoid:**
- Deleting standard columns
- Breaking formula references
- Removing README tab
- Changing core structure significantly

### Creating Project Template

For projects with special requirements:

1. Start with ATL template
2. Make necessary modifications
3. **Save As** with new name
4. Document customizations in README
5. Share with project team

## Best Practices

### Data Quality

!!! tip "Ensure Quality Data"
    - **Be consistent:** Use dropdowns, don't type free text
    - **Be complete:** Fill all required fields
    - **Be timely:** Update within 24 hours
    - **Be accurate:** Verify locations and descriptions

### File Management

- **One master file** per project
- Store in shared location (SharePoint, Teams)
- Enable auto-save
- Create weekly backups
- Archive old versions

### Collaboration

- **Single point of entry:** BIM Manager or coordinator owns file
- **Read-only access:** Share read-only copies for review
- **Update schedule:** Define update frequency
- **Version control:** Increment version in filename when major changes made

## Maintenance

### Weekly Tasks
- [ ] Update clash log with new clashes
- [ ] Close resolved clashes
- [ ] Update action items status
- [ ] Add meeting minutes
- [ ] Refresh dashboard

### Monthly Tasks
- [ ] Archive closed items (move to separate tab)
- [ ] Review metrics and trends
- [ ] Update contact list
- [ ] Clean up notes and comments
- [ ] Backup file

### Quarterly Tasks
- [ ] Export summary report
- [ ] Archive old data
- [ ] Update template if needed
- [ ] Review process improvements

## Troubleshooting

### Formulas Not Working

**Problem:** Calculations show errors

**Solutions:**
- Don't delete rows with formulas
- Check for circular references
- Recalculate: Formulas → Calculate Now
- Restore from backup if needed

### Dropdown Lists Missing

**Problem:** Data validation dropdowns not working

**Solutions:**
- Check Data Validation settings
- Verify source lists intact
- Re-create validation if needed

### File Size Growing Too Large

**Problem:** File becomes slow or very large

**Solutions:**
- Archive closed items to separate file
- Remove unused formatting
- Compress images if any
- Delete unused worksheets

### Sharing/Permissions Issues

**Problem:** Multiple users can't edit simultaneously

**Solutions:**
- Use SharePoint/OneDrive for co-authoring
- Enable "Share Workbook" (legacy feature)
- Implement check-out/check-in process
- Consider Excel Online for real-time collaboration

## Examples

### Sample Data

The template includes sample data for demonstration:
- 10 example clashes
- 5 sample issues
- 2 meeting records
- Sample action items

**Important:** Delete or archive sample data before using for real project!

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-30 | Initial release with all core features |

## Related Resources

- [Coordination Workflows (GN-003)](../../standards/documents/gn-003.md)
- [File Naming Standard (GN-001)](../../standards/documents/gn-001.md)
- [Templates Overview](../index.md)
- [Quick Start Guide](../../getting-started/quick-start.md)

## Support

Need help with the template?

- [View FAQ](../../resources/faq.md)
- [Contact support](../../resources/support.md)

---

**Template Control**

| Version | Date | Excel Version | Changes |
|---------|------|---------------|---------|
| 1.0 | 2026-01-30 | 2019+ | Initial release |
