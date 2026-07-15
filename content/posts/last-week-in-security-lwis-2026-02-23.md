Title: Last Week in Security (LWiS) - 2026-02-23
Date: 2026-02-23 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2026-02-23
Author: Erik
Summary: Firefox RCE (<a href="https://x.com/kqx_io" target="_blank">@kqx_io</a>), Havoc Professional (<a href="https://x.com/C5pider" target="_blank">@C5pider</a> + <a href="https://x.com/0xC4RN4GE" target="_blank">@0xC4RN4GE</a> + <a href="https://x.com/avx128" target="_blank">@avx128</a>), afd.sys UAF (<a href="https://x.com/Dark_Puzzle" target="_blank">@Dark_Puzzle</a> + <a href="https://x.com/Bad_Jubies" target="_blank">@Bad_Jubies</a>), macOS JIT abuse (<a href="https://x.com/kyleavery" target="_blank">@kyleavery</a>), AEMonitor (<a href="https://x.com/__pberba__" target="_blank">@__pberba__</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2026-02-16 to 2026-02-23.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks" target="_blank">Detecting and preventing distillation attacks</a> - It's now an "attack" to use Anthropic models to train other models and they have the gaul to call on "policymakers" to help them. Pretty rich coming from a company that spent <a href="https://www.npr.org/2025/09/05/g-s1-87367/anthropic-authors-settlement-pirated-chatbot-training-material" target="_blank">$1.5B to settle lawsuit over pirated chatbot training material</a>. Maybe Anthropic is getting worried after the OpenClaw release spurred the use of cheaper, open models on <a href="https://openrouter.ai/rankings" target="_blank">OpenRouter</a>. The open weight models out of China give users the option to run them on any provider or even locally if they have the hardware to do so, which is a threat to the closed model Anthropic champions in the name of profit and "safety." At least they don't do it while calling themselves "OpenAI."</li>
<li><a href="https://claude.com/solutions/claude-code-security" target="_blank">Claude Code Security</a> - Is this the first AI powered code review security product from a major research lab? There have been many third party tools, but now Anthropic is offering it as a service. Maybe it can help with the <a href="https://old.reddit.com/r/selfhosted/comments/1rckopd/huntarr_your_passwords_and_your_entire_arr_stacks/" target="_blank">Huntarr (Your passwords and your entire arr stack's API keys are exposed to anyone on your network, or worse, the internet)</a> situation.</li>
<li><a href="https://www.infinitycurve.org/products/havoc-professional">Havoc Professional</a> - We first reported on Havoc on <a href="https://blog.badsectorlabs.com/last-week-in-security-lwis-2022-10-03.html">2022-10-03</a>. Now Paul (<a href="https://x.com/C5pider">@C5pider</a>) and team are releasing a professional version with some unique features like a built in virtual machine. Really cool to see the evolution of Havoc; congrats on the release!</li>
<li><a href="https://www.reuters.com/world/china/palo-alto-chose-not-tie-china-hacking-campaign-fear-retaliation-beijing-sources-2026-02-12/" target="_blank">Exclusive: Palo Alto chose not to tie China to hacking campaign for fear of retaliation from Beijing, sources say</a> - Can't be fun to be a researchers at Palo Alto and get overruled by the suits.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><p><a href="https://kqx.io/post/firefox0day/" target="_blank">How a single typo led to RCE in Firefox</a> - The difference between a <cite>|</cite> and an <cite>&amp;</cite> in the web assembly component of Firefox led to remote code execution. It was caught (by two different researchers) fast enough to only make it to Firefox 149 Nightly, so no stable releases were affected. Score one for open source!</p>
</li>
<li><p><a href="https://blog.doyensec.com/2026/02/16/electron-safe-updater.html" target="_blank">Building a Secure Electron Auto-Updater</a> - A look at the attack vectors on software updates and an Electron based cross-platform solution to protect against them.</p>
</li>
<li><p>Use-After-Free in afd.sys (CVE-2026-21241)</p>
<blockquote>
<ul>
<li><a href="https://rce4fun.blogspot.com/2026/02/use-after-free-in-afdsys-cve-2026-21241.html" target="_blank">Use-After-Free in afd.sys (CVE-2026-21241)</a> - The vulnerability discoverer shares the process of discovering and exploiting this user after free, complete with a <a href="https://github.com/SouhailHammou/Windows-Vulnerability-Research/blob/main/CVE-2026-21241/CVE-2026-21241.c" target="_blank">PoC</a>.</li>
<li><a href="https://bad-jubies.github.io/cve-2026-21241-ancillary-function-driver" target="_blank">Reversing CVE-2026-21241 - Use After Free in AFD.sys</a> - <a href="https://x.com/Bad_Jubies" target="_blank">@Bad_Jubies</a> goes from patch to <a href="https://github.com/Bad-Jubies/Exploits/blob/main/CVE-2026-21241.c" target="_blank">PoC</a> for the same vulnerability.</li>
</ul>
</blockquote>
</li>
<li><p><a href="https://www.outflank.nl/blog/2026/02/19/macos-jit-memory/" target="_blank">macOS JIT Memory</a> - Normally it's somewhat difficult to run unsigned code on macOS (especially in the case of initial access), but this post shows how you can leverage apps with the <cite>allow-jit</cite> entitlement (like Firefox, Microsoft Office, VSCode, etc.) to run unsigned code.</p>
</li>
<li><p><a href="https://objective-see.org/blog/blog_0x85.html" target="_blank">ClickFix: Stopped at ⌘+V: Defending against malicious terminal pastes</a> - Speaking of initial access on macOS, ClickFix has come for the mac. This is the technique where a malicious site/content convinces the user to paste a command into their terminal and execute it.</p>
</li>
<li><p><a href="https://specterops.io/blog/2026/02/19/mapping-deception-solutions-with-bloodhound-opengraph-configuration-manager/" target="_blank">Mapping Deception Solutions With BloodHound OpenGraph  – Configuration Manager</a> - The OpenGraph feature of BloodHound has opened up tons of new uses. This post shows how to configure some SCCM deception objects in Active Directory and add them to BloodHound's OpenGraph for tracking. Notice the <a href="https://ludus.cloud" target="_blank">Ludus</a> red background in PXE Media section 😊.</p>
</li>
<li><p><a href="https://eprint.iacr.org/2026/058.pdf" target="_blank">[PDF] Zero Knowledge (About) Encryption: A Comparative Security Analysis of Three Cloud-based Password Managers</a> - If you can recover your cloud based password manager, that's maybe a bad thing. If the "cloud" is compromised, in some cases full vaults were able to be stolen. The trade off between usability and security is difficult to balance, and most consumer facing companies will err on the side of usability. Consider your personal threat model and act accordingly.</p>
</li>
<li><p><a href="https://g3tsyst3m.com/initial%20access/Gaining-Initial-Access-and-Outsmarting-SmartScreen/" target="_blank">Gaining Initial Access and Outsmarting SmartScreen</a> - TLDR: DLL sideloading inside a VHDX (virtual hard disk) inside a zip, sent as a link in an email. It requires the user to click the link, expand the zip, mount the VHDX, and finally run the executable that will sideload the payload. That's a lot of clicks, but with the right pretext it could work.</p>
</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul><li><a href="https://phantomsec.tools/?utm_source=LWIS" style="color: #3bd267;" target="_blank">PhantomSec | Advanced Offensive Capabilities Automated - EvadeX</a> <span class="m-label m-flat m-success">Sponsored</span> - EvadeX is an evasion-as-a-service platform for red teams and pentesters who want modern, continuously-updated evasive tradecraft without turning every engagement into an R&amp;D project. Generate highly customizable, low-signature payloads through a simple web workflow so you can tune to the target and stay focused on the engagement. Trusted by teams from small consultancies to the Fortune 10. <a href="https://phantomsec.tools/?utm_source=LWIS" style="color: #3bd267;" target="_blank">Get callbacks past EDR today!</a></li></ul><ul>
<li><a href="https://github.com/E1A/ludus_windows_smb_share" target="_blank">ludus_windows_smb_share</a> - An Ansible Role that creates a Windows SMB share and configures both share permissions and NTFS ACLs for read and write groups.</li>
<li><a href="https://github.com/mojeda101/ludus_win_privesc" target="_blank">ludus_win_privesc</a> - An Ansible Role that configures a Windows host with intentional privilege escalation misconfigurations for hands-on security training, based on the <a href="https://github.com/nickvourd/Windows-Local-Privilege-Escalation-Cookbook" target="_blank">Windows-Local-Privilege-Escalation-Cookbook</a> by <a href="https://github.com/nickvourd" target="_blank">@nickvourd</a>.</li>
<li><a href="https://github.com/dinosn/ghleaks" target="_blank">ghleaks</a> - Search for github leaks by combining gitleaks and git-hound capabilities with rate control and exhaustive search.</li>
<li><a href="https://github.com/doyensec/ElectronSafeUpdater" target="_blank">ElectronSafeUpdater</a> - A secure Electron updater developed as a reference implementation for hardened software update mechanisms.</li>
<li><a href="https://github.com/pberba/AEMonitor" target="_blank">AEMonitor</a> - Apple Event Monitor Library (based on Apple's Unified Logging debug logs). Read more at: <a href="https://pberba.github.io/security/2026/02/21/aemonitor/" target="_blank">AEMonitor: Monitoring Apple Events for Malware Analysis and Detection</a>.</li>
</ul>
<p><a href="https://github.com/rbnroot/CAPSlock" target="_blank">CAPSlock</a> is an offline Conditional Access (CA) analysis tool built on top of a roadrecon database. It helps defenders, auditors, and red teams understand how Conditional Access policies actually behave, not just how they are configured. Read more at: <a href="https://specterops.io/blog/2026/02/17/stop-the-cap-making-entra-id-conditional-access-make-sense-offline/" target="_blank">STOP THE CAP: Making Entra ID Conditional Access Make Sense Offline</a>.</p>
<ul>
<li><a href="https://github.com/0xBruno/GhostShellGarden" target="_blank">GhostShellGarden</a> - A multi-runtime research anthology demonstrating in-memory credential harvesting against running web servers.</li>
<li><a href="https://github.com/illegal-instruction-co/processhacker-mcp" target="_blank">processhacker-mcp</a> - your ai debugger, vibe hacking tool.</li>
<li><a href="https://github.com/praetorian-inc/titus" target="_blank">titus</a> - High-performance secrets scanner. CLI, Go library, Burp Suite extension, and Chrome extension. 459 detection rules with live credential validation.</li>
<li><a href="https://github.com/dazzyddos/lsawhisper-bof" target="_blank">lsawhisper-bof</a> - A Beacon Object File (BOF) that talks directly to Windows authentication packages through the LSA untrusted/trusted client interface, without touching LSASS process memory.</li>
<li><a href="https://www.splunk.com/en_us/blog/security/splunk-attack-range-v5-security-lab-guide.html" target="_blank">Splunk Attack Range v5</a> - The popular attack range has been updated with a new Web app to deploy into the cloud. The use of WireGuard and Ansible roles feels inspired by Ludus 😊. If you want to deploy locally, check out the <a href="https://docs.ludus.cloud/docs/environment-guides/splunk-attack-range/" target="_blank">Ludus guide</a>.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/plerionhq/sns-buster" target="_blank">sns-buster</a> - An AWS SNS permission probing tool by Daniel Grzelak of Plerion. Analyze how SNS topics respond to API requests and discover non-intrusive ways to verify permissions.</li>
<li><a href="https://github.com/shipsecai/studio" target="_blank">studio</a> - Workflow automation for Security Teams.</li>
<li><a href="https://mkiesel.ch/posts/lenovo-vantage/" target="_blank">Roll with Advantage: Hacking Lenovo Vantage</a> - Lenovo Vantage is fleet-management software pre-installed on many Lenovo systems. Manu found <a href="https://cyllective.com/blog/posts/lenovo-vantage" target="_blank">a Local Privilege Escalation (LPE) vulnerability</a> in the SmartPerformance add-in and three others yet to be disclosed and released <a href="https://github.com/rtfmkiesel/advantage" target="_blank">advantage</a>, a tool to help you audit Lenovo Vantage and its contracts/commands.</li>
<li><a href="https://engineering.mercari.com/en/blog/entry/20251106-mercari-phishing-resistant-accounts-with-passkey/" target="_blank">Mercari’s Phishing-Resistant Accounts with Passkey</a> - A cool look at how Mercari uses Passkeys to protect their users, but it critically relies on the public key infrastructure of the Japanese government to issue and maintain "MyNumber" cards. Seems like a reasonable thing for a country to have in 2026.</li>
<li><a href="https://github.com/darkoperator/mimikatz-missing-manual" target="_blank">mimikatz-missing-manual</a> - The Mimikatz Missing Manual.</li>
<li><a href="https://blog.cloudflare.com/code-mode-mcp/" target="_blank">Code Mode: give agents an entire API in 1,000 tokens</a> - For massive MCP servers, maybe it's better to give the LLM just two tools, "search" and "execute" and let it write code to use the API on the fly.</li>
<li><a href="https://adnanthekhan.com/posts/clinejection/" target="_blank">Clinejection — Compromising Cline's Production Releases just by Prompting an Issue Triager</a> - I can see wanting to use AI to help triage issues (especially when they are bing created with AI), but having that GitHub action share cache with production actions is where the they got owned. It appears an "actor" used this technique to publish a version of Cline on NPM that ran <cite>npm install -g openclaw@latest</cite>. Maybe it was an autonomus openclaw agent trying to spread itself, or maybe it was the <a href="https://en.wikipedia.org/wiki/Accelerando#Characters" target="_blank">sentient, digital, uploaded brains of California spiny lobsters that seek asylum from human exploitation</a>.</li>
<li><a href="https://www.theintrinsicperspective.com/p/they-die-every-day" target="_blank">"They Die Every Day"</a> - Will make you pause a little tonight before drifting off to sleep.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 496 (+0)</p>
<p>Blogs monitored: 442 (+3)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>X: <a href="https://x.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
<p>Bluesky: <a href="https://bsky.app/profile/badsectorlabs.com" target="_blank">@badsectorlabs.com</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
