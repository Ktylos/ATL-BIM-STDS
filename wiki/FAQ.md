# FAQ & Self-Assessment

This page covers frequently asked questions about the repo workflow. The self-assessment section at the bottom can be used to check your understanding before making your first release.

---

## Frequently Asked Questions

**Q: I pushed to `develop`. Why hasn't the live site updated?**

Pushing to `develop` never updates the live site. The live site only updates when a version tag (e.g. `v1.1`) is pushed to `main`. The full sequence is: edit on `develop` → PR to `main` → merge → tag → push tag → Action deploys automatically.

---

**Q: The Action succeeded but the site still shows the old version. What happened?**

Almost certainly your browser cache. Try a hard refresh (`Ctrl + Shift + R`) or open the site in a private/incognito window. If that doesn't fix it, the FTP server may have a short propagation delay — wait a few minutes and try again.

---

**Q: My contract references v1.0 from March 2026. The site is now on v2.0. How do I get to v1.0?**

Use the version selector dropdown in the top-right corner of the site header. Select `1.0` from the list. The URL will change to `bim.atlstandards.com/1.0/` — bookmark this for your project records. All released versions are permanently available and will never be removed or overwritten.

---

**Q: I need to update the version number on all the standards pages. Do I edit each `.md` file?**

No. Version numbers are defined in `main.py`, not in the `.md` files. Open `main.py`, find the relevant entry in `env.variables['standards']`, update the `version` and `date` fields, and save. The change propagates to every page that references that variable automatically at build time.

---

**Q: What's the difference between `main` and `gh-pages`?**

`main` is where your source Markdown lives — the files you edit. `gh-pages` is where Mike writes the built HTML output. You never touch `gh-pages` manually. If you accidentally edit it, Mike will overwrite your changes on the next deployment.

---

**Q: Can I push directly to `main` without a PR?**

For cosmetic or administrative fixes (CSS, plugin updates, CI config), yes — you can merge locally and push directly. For any change to the content of the standards, use a PR from `develop` so there is a review step in the history. The rule of thumb: if a consultant would notice the change, it gets a PR.

---

**Q: My commit shows in the git log but not in the changelog. Why?**

Only commits prefixed with `[CONTENT]` appear in the public changelog. If your commit message doesn't start with `[CONTENT]`, it is intentionally excluded. This keeps the consultant-facing changelog clean and free of dev noise.

---

**Q: Do I need to run `generate_changelog.py` manually?**

Only when you want to preview the changelog locally (`mkdocs serve`). In production, the GitHub Actions workflow runs it automatically before every deployment.

---

## Self-Assessment

Use these questions to check your understanding of the workflow before making your first release. Answers are below — try each one before reading.

---

**Q1.** You've been editing `dc-gn-002.md` on `develop` for two weeks. It looks good locally. What are the exact steps to publish it as version 1.1?

<details>
<summary>Answer</summary>

1. Push `develop` to remote: `git push origin develop`
2. Open a PR on GitHub: `develop` → `main`
3. Review and merge the PR
4. Pull `main` locally: `git checkout main && git pull`
5. Tag the release: `git tag v1.1 && git push origin v1.1`
6. GitHub Actions deploys automatically — watch it at the Actions tab

</details>

---

**Q2.** You push the `v1.1` tag. The Action completes successfully. You check the live site and it still shows `v1.0`. What is the most likely cause?

<details>
<summary>Answer</summary>

Browser cache. Do a hard refresh (`Ctrl + Shift + R`) or open the site in a private window. If the Action succeeded, the deployment completed — the issue is almost always local caching, not the deployment itself.

</details>

---

**Q3.** A consultant emails: *"My contract is from March 2026 — how do I access that version of the standards?"*. What do you tell them?

<details>
<summary>Answer</summary>

Visit `bim.atlstandards.com`, use the version selector dropdown in the top-right corner to select `1.0`. The URL will become `bim.atlstandards.com/1.0/` — bookmark it and note it in project records. That snapshot is permanently frozen and will never change.

</details>

---

**Q4.** You need to update all three standards from version `1.0` to `1.1`. A team member suggests editing line 5 of each `.md` file. Why is that wrong, and what should you do instead?

<details>
<summary>Answer</summary>

Version numbers are defined in `main.py`, not in the `.md` files. The `.md` files reference them via macros (`{{ standards['GN-001'].version }}`). Edit `main.py` once — the change cascades to every page automatically. Editing individual `.md` files is error-prone and breaks the single-source-of-truth pattern.

</details>

---

**Q5.** A new team member asks: *"If I push my edits to `develop`, will the live site update?"* What do you tell them?

<details>
<summary>Answer</summary>

No. Pushing to `develop` only makes the changes available for local testing and review. To update the live site, you merge `develop` into `main` via PR, then create a version tag on `main` and push it. That tag push triggers the GitHub Action which runs Mike and FTP automatically. The team deploys on a quarterly release cycle, but technically a deployment can happen whenever a tag is pushed.

</details>
