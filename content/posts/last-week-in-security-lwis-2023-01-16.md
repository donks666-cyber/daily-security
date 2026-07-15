Title: Last Week in Security (LWiS) - 2023-01-16
Date: 2023-01-16 18:25
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-01-16
Author: Erik
Summary: SCCM relay to takeover (<a href="https://twitter.com/_mayyhem" target="_blank">@_Mayyhem</a>), LAPS 101 (<a href="https://twitter.com/mega_spl0it" target="_blank">@mega_spl0it</a>), Sliver vs Havoc (<a href="https://twitter.com/naw" target="_blank">@Naw</a>), Defender LPE (<a href="https://twitter.com/pixiepointsec" target="_blank">@pixiepointsec</a>), CircleCI post mortem, ASRmageddon, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2023-01-09 to 2023-01-16.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://security.googleblog.com/2023/01/supporting-use-of-rust-in-chromium.html" target="_blank">Supporting the Use of Rust in the Chromium Project</a>. Rust is coming, and its taking down memory safety bugs/exploits as its spreads.</li>
<li><a href="https://security.googleblog.com/2023/01/sustaining-digital-certificate-security_13.html" target="_blank">Sustaining Digital Certificate Security - TrustCor Certificate Distrust</a>. As <a href="https://www.washingtonpost.com/technology/2022/11/30/trustcor-internet-authority-mozilla/" target="_blank">previously reported</a>, reporting from the Washington Post has led to questions about TrustCor, and this is the official announcement that Google is dropping them from the Chrome CA root store.</li>
<li><a href="https://circleci.com/blog/jan-4-2023-incident-report/" target="_blank">CircleCI incident report for January 4, 2023 security incident</a>. There is still some detail missing (no detail on how they know "the third party extracted encryption keys from a running process" and no public samples of the malware), but the incident report does shed light on how all of CircleCI was compromised. A single employee had their SSO session cookie stolen, and the production system fell. Now is a good time to tabletop what would happen at your company if your lead engineer had their SSO cookie stolen... In the meantime, follow this <a href="https://www.wiz.io/blog/hunting-for-signs-of-persistence-in-the-cloud-an-ir-guide" target="_blank">IR guide</a>.</li>
<li><a href="https://www.doioig.gov/sites/default/files/2021-migration/Final%20Inspection%20Report_DOI%20Password_Public.pdf" target="_blank">[PDF] P@s$w0rds at the U.S. Department of the Interior: Easily Cracked Passwords, Lack of Multifactor Authentication, and Other Failures Put Critical DOI Systems at Risk</a>. People still choose terrible passwords. Arm your users with a password manager and teach them how to use it. Enforce MFA everywhere you can. Hand out hardware tokens and enforce their use. With the rise of passkeys, a passwordless future is possible, but legacy password support will be around for at least the next 25 years.</li>
<li><a href="https://techcommunity.microsoft.com/t5/microsoft-defender-for-endpoint/recovering-from-attack-surface-reduction-rule-shortcut-deletions/ba-p/3716011" target="_blank">Recovering from Attack Surface Reduction rule shortcut deletions</a>. Friday the 13th saw Attack Surface Reduction users get an updated definition that "resulted in the deletion of files that matched the incorrect detection logic primarily impacting Windows shortcut (.lnk) files." This manifested itself with users calling the help desk stating that "all my apps are gone," which sounds a lot like ransomware. Thanks Microsoft. <a href="https://github.com/microsoft/MDE-PowerBI-Templates/blob/master/ASR_scripts/AddShortcuts.ps1" target="_blank">AddShortcuts.ps1</a> might help recover shortcuts for users.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://posts.specterops.io/sccm-site-takeover-via-automatic-client-push-installation-f567ec80d5b1" target="_blank">SCCM Site Takeover via Automatic Client Push Installation</a>. SCCM is perhaps the best lateral movement technique against organizations that use it, but the issue for red teams was compromising the primary server. With this research, it's possible to land a single phish (get any authenticated domain user), and coerce/relay your way to SCCM site takeover, which enables you to push out arbitrary executables or run scripts on every machine managed by SCCM. If ransomware crews aren't already doing this, they soon will be. Protect the MSSQL endpoints that SCCM use!</li>
<li><a href="https://thalpius.com/2023/01/16/microsoft-defender-for-identity-lateral-movement-from-forest-to-forest-without-a-forest-trust/" target="_blank">Microsoft Defender for Identity Lateral Movement from Forest to Forest without a Forest trust</a>. Using Defender to jump between untrusted forests? Awesome.</li>
<li><a href="https://blog.nviso.eu/2023/01/10/malware-based-attacks-on-atms-a-summary/" target="_blank">Malware-based attacks on ATMs - A summary</a>. Perhaps not the most relevant article for red/blue teams, but still interesting.</li>
<li><a href="https://www.trustedsec.com/blog/a-lapse-in-judgement/" target="_blank">A LAPS(e) in Judgement</a>. A good overview of the local admin password solution (LAPS) for Windows domains, how to set it up, how to abuse it, and how to detect that abuse.</li>
<li><a href="https://github.com/DesktopECHO/T95-H616-Malware" target="_blank">T95-H616-Malware</a>. "Pre-Owned" malware in ROM on T95 Android TV Box (AllWinner H616).</li>
<li><a href="https://git.culbertreport.com/posts/Sliver-vs-Havoc/" target="_blank">Sliver vs havoc</a>. If you aren't familiar with two of the more popular non-Cobalt Strike C2s that are available, this post breaks them down.</li>
<li><a href="https://www.pixiepointsecurity.com/blog/nday-cve-2021-31985.html" target="_blank">CVE-2021-31985: Exploiting the Windows Defender AsProtect Heap Overflow Vulnerability</a>. The irony of using Windows Defender to get a SYSTEM shell is delicious.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/jconwell/secret_handshake" target="_blank">secret_handshake</a> - A prototype malware C2 channel using x509 certificates over mTLS.</li>
<li><a href="https://github.com/jackmichalak/phishim" target="_blank">phishim</a> is a phishing tool which reduces configuration time and bypasses most types of MFA by running a chrome tab on the server that the user unknowingly interacts with.</li>
<li><a href="https://github.com/OtterHacker/CoffLoader" target="_blank">CoffLoader</a> - an implementation of in-house CoffLoader supporting CobaltStrike standard BOF and BSS initialized variables.</li>
<li><a href="https://github.com/silverfort-open-source/latma" target="_blank">latma</a> -  Lateral movement analyzer (LATMA) collects authentication logs from the domain and searches for potential lateral movement attacks and suspicious activity. The tool visualizes the findings with diagrams depicting the lateral movement patterns.</li>
<li><a href="https://github.com/maldevel/gophish" target="_blank">gophish</a> - GoPhish automation.</li>
<li><a href="https://seclists.org/oss-sec/2023/q1/20" target="_blank">CVE-2023-0179: Linux kernel stack buffer overflow in nftables: PoC and writeup</a>. PoC has been pulled for the time being, but as this effects Linux from ~2019 and later, it could be a pretty widespread LPE and potentially some LAN crashes or RCE.</li>
<li><a href="https://www.localpotato.com/" target="_blank">LocalPotato is coming soon!</a> - Watch this space.</li>
<li><a href="https://bugs.chromium.org/p/project-zero/issues/detail?id=2361" target="_blank">Issue 2361: XNU race condition in vm_map_copy_overwrite_unaligned allows writing to read-only mappings</a>. Ian Beer drops his "MacDirtyCow" which is already being used in the jailbreaking scene to do non-persistent tweaks.</li>
<li><a href="https://github.com/Aetsu/OffensivePipeline" target="_blank">OffensivePipeline</a> allows you to download and build C# tools, applying certain modifications in order to improve their evasion for Red Team exercises. Version 2 just dropped.</li>
<li><a href="https://docs.harpia.io/blog/open-sourcing-incident-management-system" target="_blank">Open Sourcing Incident Management system</a>. The HARP incident management system, designed to help teams quickly and effectively respond to and resolve any incidents that may occur, specifically in the tech industry, is now open source!</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/vullabs/Crassus" target="_blank">Crassus</a> - Windows privilege escalation discovery tool</li>
<li><a href="https://github.com/Bw3ll/ShellWasp" target="_blank">ShellWasp</a> is a tool to help build shellcode that utilizes Windows syscalls, while overcoming the portability problem associated with Windows syscalls. ShellWasp is built for 32-bit, WoW64.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 423 (+1)</p>
<p>Blogs monitored: 333 (+3)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
