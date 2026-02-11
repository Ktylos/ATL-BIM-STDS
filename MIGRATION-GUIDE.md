# Migration Guide: Moving to Clean Repository

## ✅ What's Been Done

A clean repository structure has been created in: **ATL-STANDARDS-DEPLOY-Clean/**

### What's Included:

✅ All 3 standards documents (dc-gn-001, dc-gn-002, dc-gn-003)
✅ All template documentation (tp-gn-001, tp-gn-002)
✅ Airport branding (logos, custom CSS)
✅ Source files (native Word/Revit/Excel)
✅ Simplified deployment workflow (single file)
✅ Clean mkdocs.yml (NO GitHub integrations)
✅ Simplified main.py (NO GitHub macros)
✅ Clean home and support pages (NO GitHub references)
✅ Changelog generator
✅ Comprehensive README

### What's Been Removed:

❌ Azure pipelines (azure-pipelines.yml)
❌ Multiple deployment workflows (7 old workflows → 1 clean workflow)
❌ GitHub Issues/Discussions references
❌ GitHub release links
❌ Feedback page (relied on GitHub)
❌ Old documentation files (12+ markdown guides)
❌ Unused Python scripts (remove_escapes.py, deploy-manual.ps1)
❌ Development reference files

---

## 🚀 Migration Steps

### 1. Create New Repository on GitHub Enterprise

\\\
1. Go to your GitHub Enterprise organization
2. Click 'New repository'
3. Name: ATL-STANDARDS-DEPLOY
4. Description: Official BIM standards for ATL Planning & Development
5. Private: Yes
6. DEFAULT BRANCH: main (important!)
7. Do NOT initialize with README (we have one)
8. Click 'Create repository'
\\\

### 2. Initialize Clean Repository

\\\powershell
cd ATL-STANDARDS-DEPLOY-Clean

# Initialize git
git init

# Add all files
git add .

# Initial commit
git commit -m 'Initial commit - Clean ATL BIM Standards v1.0'

# Add remote
git remote add origin https://github.com/EMU-WSP-Internal-Repos/ATL-STANDARDS-DEPLOY.git

# Push to main branch
git branch -M main
git push -u origin main
\\\

### 3. Configure GitHub Secrets

In the new repository:

\\\
1. Go to Settings → Secrets and variables → Actions
2. Click 'New repository secret'
3. Add two secrets:
   - Name: FTP_USERNAME
     Value: ktylos@atlstandards.com
   
   - Name: FTP_PASSWORD
     Value: [your FTP password]
4. Click 'Add secret'
\\\

### 4. Test Deployment

\\\powershell
# Make a small test change
echo '<!-- test -->' >> README.md

# Commit and push
git add README.md
git commit -m 'test: Verify deployment workflow'
git push origin main

# Watch GitHub Actions:
# Go to Actions tab in GitHub
# Verify 'Deploy to bim.atlstandards.com' workflow runs
# Check it completes successfully
\\\

### 5. Verify Site

Visit: **https://bim.atlstandards.com**

Check:
- [ ] Site loads correctly
- [ ] All 3 standards pages work
- [ ] Templates pages work
- [ ] Support page loads
- [ ] Changelog page exists
- [ ] Images/logos display
- [ ] Search works
- [ ] Mobile view looks good

### 6. Upload Release Package

\\\powershell
# Add your release zip file
Copy-Item 'path\to\ATL-STANDARDS-DEPLOY-v1.0.zip' -Destination 'docs\downloads\'

# Commit and deploy
git add docs\downloads\ATL-STANDARDS-DEPLOY-v1.0.zip
git commit -m 'feat: Add v1.0 release package'
git push origin main
\\\

After deployment, test download:
**https://bim.atlstandards.com/downloads/ATL-STANDARDS-DEPLOY-v1.0.zip**

### 7. Create First Release Tag

\\\powershell
# Create v1.0.0 release tag
git tag -a v1.0.0 -m 'Initial Public Release
- GN-001: File Naming and Organization v1.0
- GN-002: BIM Modeling Best Practices v1.0
- GN-003: Coordination Workflows v1.0
- Complete documentation site'

# Push tag
git push origin v1.0.0
\\\

### 8. Archive Old Repository

Option A: Delete the old repo
- Only if you're confident everything works

Option B: Archive it
1. Go to old repo settings
2. Scroll to 'Danger Zone'
3. Click 'Archive this repository'
4. Confirm - it becomes read-only

Option C: Keep it as backup
- Rename it: ATL-BIM-GitDocs-Deployment-OLD
- Update description: 'ARCHIVED - See ATL-STANDARDS-DEPLOY'

---

## 📝 Daily Workflow (After Migration)

### Editing Standards

\\\powershell
# 1. Make changes to markdown files in docs/
# 2. Test locally
mkdocs serve

# 3. Commit with descriptive message
git add .
git commit -m 'docs: Update coordination workflow in GN-003'

# 4. Push (auto-deploys)
git push origin main
\\\

### Quarterly Release

\\\powershell
# 1. Update version in main.py
# 2. Create release tag
git tag -a v2026.Q2 -m 'Q2 2026 Release'

# 3. Push everything
git push origin main
git push origin v2026.Q2
\\\

---

## 🆘 Troubleshooting

### Deployment Fails

Check GitHub Actions logs:
1. Go to 'Actions' tab
2. Click the failed workflow run
3. Expand steps to see errors

Common issues:
- FTP credentials wrong → Update secrets
- Build errors → Run \mkdocs build --strict\ locally
- Python version → Workflow uses 3.11

### Site Not Updating

1. Check GitHub Actions completed successfully
2. Wait 2-3 minutes for FTP transfer
3. Hard refresh browser (Ctrl+Shift+R)
4. Clear browser cache

### Missing Files

If files don't deploy:
1. Verify file exists in \site/\ after build
2. Check .gitignore doesn't exclude it
3. Ensure file is committed to git

---

## 📋 Checklist

Before going live:

- [ ] New repository created with 'main' as default branch
- [ ] FTP secrets configured
- [ ] Clean repository initialized and pushed
- [ ] Deployment workflow runs successfully
- [ ] Site loads at bim.atlstandards.com
- [ ] All pages accessible
- [ ] Release package uploaded and downloadable
- [ ] Changelog generates correctly
- [ ] Search functionality works
- [ ] Mobile view tested
- [ ] Old repository archived/renamed
- [ ] Team notified of new repository location
- [ ] Documentation links updated

---

## 🎉 You're Done!

You now have:
✅ Clean, professional repository structure
✅ Proper 'main' branch naming
✅ No Azure or GitHub integration references
✅ Single, simple deployment workflow
✅ Easy-to-maintain codebase
✅ Clear documentation

**Next:** Focus on content - the technical infrastructure is solid!


