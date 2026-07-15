Title: Last Week in Security (LWiS) - 2024-04-08
Date: 2024-04-08 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-04-08
Author: Erik
Summary: Evilginx + GoPhish (<a href="https://twitter.com/mrgretzky" target="_blank">@mrgretzky</a>), Ghostwriter updates (<a href="https://twitter.com/cmaddalena" target="_blank">@cmaddalena</a>), Intune EPM privesc (<a href="https://twitter.com/synzack21" target="_blank">@synzack21</a> + team) 🎣 page bot defense (<a href="https://twitter.com/fin3ss3g0d" target="_blank">@fin3ss3g0d</a>), and more!

<aside class="m-note m-success">
<h3>XZ Backdoor Role</h3>
<p>Get hands on with the XZ backdoor with the new <a href="https://github.com/badsectorlabs/ludus_xz_backdoor" target="_blank">xz_backdoor role</a> for Ludus.</p>
<p>Commando VM, Flare VM, and REMnux templates and roles for Ludus dropped last week as well!</p>
<p>Learn more about Ludus at <a href="https://ludus.cloud" target="_blank">ludus.cloud</a>.</p>
</aside>
<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-04-01 to 2024-04-08.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://source.android.com/docs/security/bulletin/pixel/2024-04-01" target="_blank">Pixel Update Bulletin—April 2024</a> - "There are indications that the following may be under limited, targeted exploitation." Update those Pixels!</li>
<li><a href="https://www.wired.com/story/google-chrome-incognito-mode-data-deletion-settlement/" target="_blank">The Incognito Mode Myth Has Fully Unraveled</a> - Google settles a lawsuit about Incognito Mode by agreeing to delete "billions of data records" the company collected while users browsed the web using Incognito mode. This implies that the data was tagged as being collected while the browser was in incognito mode.</li>
<li><a href="https://blog.chromium.org/2024/04/fighting-cookie-theft-using-device.html" target="_blank">Fighting cookie theft using device bound sessions</a> - Cookie theft from Chrome based browsers could get more difficult on computers with a TPM.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://fin3ss3g0d.net/index.php/2024/04/08/evilgophishs-approach-to-advanced-bot-detection-with-cloudflare-turnstile/" target="_blank">EvilGophish's Approach to Advanced Bot Detection with Cloudflare Turnstile</a> - Using commercial products designed to stop bots to protect phishing infrastructure from scanners and bots is clever. Why re-invent the wheel?</li>
<li><a href="https://github.blog/2024-04-03-security-research-without-ever-leaving-github-from-code-scanning-to-cve-via-codespaces-and-private-vulnerability-reporting/" target="_blank">Security research without ever leaving GitHub: From code scanning to CVE via Codespaces and private vulnerability reporting</a> - You can do CodeQL scanning and even development in Codespaces all from your browser. The era of the centralized, time-share, computer is back! Mainframes got replaced with "the cloud" and web browsers are the new IBM 3270 terminals.</li>
<li><a href="https://posts.specterops.io/ghostwriter-v4-1-the-custom-fields-update-fe07f7dda293" target="_blank">Ghostwriter v4.1: The Custom Fields Update</a> - The Ghostwriter documentation automation web-app just got a lot more customizable, as you can extend the data models easily in 4.1, and now any formatted text fields support Jinja2 templates!</li>
<li><a href="https://posts.specterops.io/getting-intune-with-bugs-and-tokens-a-journey-through-epm-013b431e7f49" target="_blank">Getting Intune with Bugs and Tokens: A Journey Through EPM</a> - 4 Specter Ops hackers looked into Microsoft Intune Endpoint Privilege Management (EPM) and found a privilege escalation vulnerability.</li>
<li><a href="https://lutrasecurity.com/en/articles/kobold-letters/" target="_blank">Kobold Letters - Why HTML emails are a risk to your organization</a> - You can use the <cite>kobold-letter</cite> class to hide text in an email until it is forwarded. A powerful primitive for phishing.</li>
<li><a href="https://www.rtl-sdr.com/em-eye-eavesdropping-on-security-camera-via-unintentional-rf-emissions/" target="_blank">Em Eye: Eavesdropping on Security Camera via Unintentional Rf Emissions</a> - This is pretty incredible. Using just a software defined radio, amplifier, and antenna the researchers could recreate images from many cameras with decent fidelity at up to 5.5 meters away. Code is available at: <a href="https://github.com/longyan97/EMEye_Tutorial" target="_blank">EMEye_Tutorial</a>.</li>
<li><a href="https://habr.com/ru/companies/ru_mts/articles/804789/" target="_blank">From HTTP to RCE. How to leave a backdoor in IIS</a> - This one has to be translated to English but it's still a good write up on IIS webshells.</li>
<li><a href="https://www.scip.ch/en/?labs.20240404" target="_blank">Foreign Entra Workload Identities: A Security Boundary Risk?</a> - This article explores an example of how Microsoft Entra workload identities can inadvertently extend the security boundary of a Entra tenant to a foreign tenant.</li>
<li><a href="https://redsiege.com/blog/2024/04/sshishing-abusing-shortcut-files-and-the-windows-ssh-client-for-initial-access/" target="_blank">SSHishing - Abusing Shortcut Files and the Windows SSH Client for Initial Access</a> - Windows shortcut files can be used to allow targets to SSH to you (careful) which can aid in initial access or lateral movement objectives</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://www.yubico.com/support/security-advisories/ysa-2024-01/" target="_blank">Security Advisory YSA-2024-01 YubiKey Manager Privilege Escalation</a> - "any browser windows opened by YubiKey Manager GUI may also be elevated with Administrator privileges depending on the browser in use. This issue can be used by an attacker to escalate local attacks and increase the impact of browser based attacks."</li>
<li><a href="https://github.com/MrTurvey/Burp2API" target="_blank">Burp2API</a> - Converting your Burp Suite projects into JSON APIs.</li>
<li><a href="https://github.com/eset/nimfilt" target="_blank">nimfilt</a> - A collection of modules and scripts to help with analyzing Nim binaries.</li>
<li><a href="https://breakdev.org/evilginx-3-3-go-phish/" target="_blank">Evilginx 3.3 - Go &amp; Phish</a> - Evilginx has an official integration with GoPhish!</li>
<li><a href="https://github.com/kiber-io/apkd" target="_blank">APK Downloader</a> -  APK downloader from few sources</li>
<li><a href="https://github.com/fortra/No-Consolation" target="_blank">No-Consolation</a> -  A BOF that runs unmanaged PEs inline. Updated this week to automatically encrypt and store binaries in memory which allows multiple runs of the same binary without having to send it to target each time.</li>
<li><a href="https://github.com/Kharos102/interceptor" target="_blank">interceptor</a> - Sample Rust Hooking Engine.</li>
<li><a href="https://github.com/20urc3/Aplos" target="_blank">Aplos</a> - Aplos an extremely simple fuzzer for Windows binaries.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/skyler-ferrante/CVE-2024-28085" target="_blank">CVE-2024-28085</a> - WallEscape vulnerability in util-linux.</li>
<li><a href="https://github.com/k1nd0ne/VolWeb" target="_blank">VolWeb</a> - A centralized and enhanced memory analysis platform.</li>
<li><a href="https://github.com/freelabz/secator" target="_blank">secator</a> is a task and workflow runner used for security assessments. It supports dozens of well-known security tools and it is designed to improve productivity for pentesters and security researchers.</li>
<li><a href="https://github.com/bcoles/kasld" target="_blank">kasld</a> - Kernel Address Space Layout Derandomization (KASLD) - A collection of various techniques to infer the Linux kernel base virtual address as an unprivileged local user, for the purpose of bypassing Kernel Address Space Layout Randomization (KASLR).</li>
<li><a href="https://github.com/d0ge/sign-saboteur" target="_blank">SignSaboteur</a> - Burp Suite extension for editing, signing, verifying various signed web tokens</li>
<li><a href="https://github.com/cgosec/Blauhaunt" target="_blank">Blauhaunt</a> -  A tool collection for filtering and visualizing logon events. Designed to help answering the "Cotton Eye Joe" question (Where did you come from where did you go) in Security Incidents and Threat Hunts</li>
<li><a href="https://github.com/evildaemond/physsec-methodology/tree/main" target="_blank">Physsec Methodology</a>  A public, open source physical security methodology</li>
<li><a href="https://github.com/invictus-ir/Microsoft-Extractor-Suite" target="_blank">Microsoft-Extractor-Suite</a> -  A PowerShell module for acquisition of data from Microsoft 365 and Azure for Incident Response and Cyber Security purposes.</li>
<li><a href="https://github.com/evild3ad/Microsoft-Analyzer-Suite" target="_blank">Microsoft-Analyzer-Suite</a> -  A collection of PowerShell scripts for analyzing data from Microsoft 365 and Microsoft Entra ID</li>
<li><a href="https://github.com/rbmm/ARL" target="_blank">ARL</a> - Injecting a DLL into a process directly from memory rather than from disk</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 425 (+0)</p>
<p>Blogs monitored: 375 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
