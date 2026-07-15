Title: Last Week in Security (LWiS) - 2024-02-12
Date: 2024-02-12 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-02-12
Author: Erik
Summary: LDAP tradecraft (<a href="https://twitter.com/domchell" target="_blank">@domchell</a>), CreateRemoteThread saftey (<a href="https://twitter.com/m417z" target="_blank">@m417z</a>), Lab automation (<a href="https://twitter.com/W9HAX" target="_blank">@W9HAX</a>), LoFP (<a href="https://twitter.com/br0k3ns0und" target="_blank">@br0k3ns0und</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-02-07 to 2024-02-12.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://kb.vmware.com/s/article/2107518" target="_blank">End Of General Availability of the free vSphere Hypervisor (ESXi 7.x and 8.x) (2107518)</a> - The end of free vSphere is a great chance to migrate to Proxmox and <a href="https://ludus.cloud" target="_blank">ludus</a> makes it easy!</li>
<li><a href="https://www.vice.com/en/article/4a388g/flipper-zero-ban-canada-hacking-car-thefts" target="_blank">Feds Want to Ban the World's Cutest Hacking Device. Experts Say It's a 'Scapegoat'</a>. Canada has banned the Flipper Zero due to an increase in car thefts where there is no evidence a Flipper Zero was used. 🧐 <a href="https://x.com/FP_Champagne/status/1755691837531078820" target="_blank">Here</a> is the tweet announcing it.</li>
<li><a href="https://www.expressvpn.com/blog/windows-app-dns-requests/" target="_blank">After a tip, ExpressVPN acts swiftly to protect customers</a> - ExpressVPN users could have experienced DNS leaks for the past 2 years. Ouch. "The bug was introduced in ExpressVPN Windows versions 12.23.1 - 12.72.0, published between May 19, 2022, and Feb. 7, 2024, and only affected those using the split tunneling feature."</li>
<li><a href="https://github.com/advisories/GHSA-27xq-w3jc-436c" target="_blank">CVE-2024-23109</a> - Yes, Fortinet again. Patch ASAP...</li>
<li><a href="https://www.wealthmanagement.com/regulation-compliance/sec-fines-firms-81m-channel-communications-lapses" target="_blank">SEC Fines Firms $81M For Off-Channel Communications Lapses</a> - "Sixteen firms are collectively on the hook for more than $81 million to settle SEC charges that they failed to preserve off-channel electronic communications." The SEC is not a fan of personal Signal chats!</li>
<li><a href="https://www.chainalysis.com/blog/ransomware-2024/" target="_blank">Ransomware Payments Exceed $1 Billion in 2023, Hitting Record High After 2022 Decline</a> - Mo money mo problems. Some interesting analytics surrounding the crime groups and their profits.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://posts.specterops.io/directory-readwrite-all-is-not-as-powerful-as-you-might-think-c5b09a8f78a8" target="_blank">Directory.ReadWrite.All Is Not As Powerful As You Might Think</a> Some deep dive into MS Graph API. Guaranteed escalations to Global Admin from RoleManagement.ReadWrite.Directory and AppRoleAssignment.ReadWrite.All roles.</li>
<li><a href="https://www.wiz.io/blog/new-attack-vectors-emerge-via-recent-eks-access-entries-and-pod-identity-features" target="_blank">New attack vectors in EKS</a> - In the recent enhancement of AWS's managed Kubernetes service, EKS, including EKS Access Entries, Policies, and Pod Identity, potential security risks are introduced, explored in the second blog post of a <a href="https://www.wiz.io/blog/eks-cluster-access-management-and-pod-identity-security-recommendations" target="_blank">series</a>, emphasizing the need for least privilege and awareness of new attack vectors.</li>
<li><a href="https://www.mdsec.co.uk/2024/02/active-directory-enumeration-for-red-teams/" target="_blank">Active Directory Enumeration for Red Teams</a> - Some post-ex LDAP fun by MDSec. There are detection considerations towards the end as well. TD;DR - Blend in where possible or else you'll stick out like a sore thumb. Assuming the defense is looking!</li>
<li><a href="https://blog.plerion.com/conditional-love-for-aws-metadata-enumeration/" target="_blank">Conditional Love for AWS Metadata Enumeration</a> - This came with a <a href="https://github.com/plerionhq/conditional-love/" target="_blank">tool release</a>. An AWS metadata enumeration tool by Daniel Grzelak of Plerion. Use it to enumerate resource tags, account IDs, and org IDs.</li>
<li><a href="https://nullg0re.com/2024/02/securing-ai-azure-machine-learning-studio/" target="_blank">Securing AI: Azure Machine Learning Studio</a> - This post covers the deployment of Machine Learning Studio, the creation of a test training model, and then attacking the AI/ML training infrastructure to deploy persistence. With AI being the hot thing right now, it's nice to see someone shelling some AI tooling.</li>
<li><a href="https://storage.googleapis.com/gweb-uniblog-publish-prod/documents/Buying_Spying_-_Insights_into_Commercial_Surveillance_Vendors_-_TAG_report.pdf" target="_blank">[PDF] Insights into Commercial Surveillance Vendors</a> - Google reports on commercial espionage. Interested read considering their role in society. "Of the 72 known in-the-wild 0-day exploits affecting Google products since mid-2014, TAG attributes 35 of these 0-days to Commercial Surveillance Vendors." That's a huge percentage!</li>
<li><a href="https://medium.com/@MorattiSec/the-crow-flies-at-midnight-exploring-red-team-persistence-via-aws-lex-chatbots-b3de1edb7893" target="_blank">The Crow Flies at Midnight — Exploring Red Team Persistence via AWS Lex Chatbots</a> - Use AWS Lex chatbot as a persistence method for your ops. The blog post details the steps to modify a Lex bot to exfiltrate credentials as well.</li>
<li><a href="https://www.bleepingcomputer.com/news/security/fake-lastpass-password-manager-spotted-on-apples-app-store/" target="_blank">Fake LastPass password manager spotted on Apple's App Store</a> - Insert creds everywhere meme. Not sure how this gets by Apple but <a href="https://blog.lastpass.com/2024/02/warning-fraudulent-app-impersonating-lastpass-currently-available-in-apple-app-store/" target="_blank">LastPass can't catch a break</a>!</li>
<li><a href="https://www.tiraniddo.dev/2024/02/sudo-on-windows-quick-rundown.html" target="_blank">Sudo On Windows a Quick Rundown</a> - The blog post provides an overview of the newly introduced <a href="https://github.com/microsoft/sudo" target="_blank">sudo</a> command in Windows Insider Preview build 26052, highlighting its implementation using User Account Control (UAC), its configuration options, and potential security vulnerabilities, including the lack of proper access control on the RPC server, despite being written mostly in Rust for enhanced security.</li>
<li><a href="https://hunt.io/blog/tracking-shadowpad-infrastructure-via-non-standard-certificates" target="_blank">Tracking ShadowPad Infrastructure Via Non-Standard Certificates</a> - Some common OPSEC mistakes. Lock down your C2! Use something like <a href="https://github.com/juanfont/headscale" target="_blank">headscale</a> if you must! <a href="https://censys.com/a-beginners-guide-to-tracking-malware-infrastructure/" target="_blank">This is another</a> related article from this week.</li>
<li><a href="https://labs.nettitude.com/blog/para-bailar-la-bambda-contributing-to-burp-suites-new-filtering-capabilities/" target="_blank">Para Bailar La Bambda: Contributing to Burp Suite's New Filtering Capabilities</a> - A simple example of how to use Bamdas in your Burp Suite workflow.</li>
<li><a href="https://m417z.com/When-is-it-generally-safe-to-CreateRemoteThread/" target="_blank">When is it generally safe to CreateRemoteThread?</a> - Short answer: probably ok if you wait for the C runtime initialization to take place and the process doesn't do any "wierd stuff."</li>
<li><a href="https://trustedsec.com/blog/offensive-lab-environments-without-the-suck" target="_blank">Offensive Lab Environments (Without the Suck)</a> - Labs are so hot right now!</li>
<li><a href="https://amitschendel.github.io/vulnerabilites/CVE-2024-20328/" target="_blank">CVE-2024-20328 - ClamAV Not So Calm</a> - Send email with a EICAR test string and properly named file, get shell?</li>
<li><a href="https://whiteknightlabs.com/2024/02/09/a-technical-deep-dive-comparing-anti-cheat-bypass-and-edr-bypass/" target="_blank">A Technical Deep Dive: Comparing Anti-Cheat Bypass and EDR Bypass</a> - The anti-anti-cheat developers and the EDR bypassers share a lot in common.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://gist.github.com/WKL-Sec/a309b10a489c51deefc128adab13eee7" target="_blank">ParentProcessValidator.cpp</a> -  This C++ code snippet demonstrates how to verify if an executable is launched by explorer.exe to enhance security during red team operations.</li>
<li><a href="https://github.com/cpu0x00/EternelSuspention" target="_blank">EternelSuspention</a> -  a simple poc showcasing the ability of an admin to suspend EDR's protected processes.</li>
<li><a href="https://github.com/Idov31/NidhoggScript" target="_blank">NidhoggScript</a> -  NidhoggScript is a tool to generate "script" file that allows execution of multiple commands for <a href="https://github.com/Idov31/Nidhogg" target="_blank">Nidhogg</a>.  Nidhogg is an all-in-one simple to use rootkit.</li>
<li><a href="https://github.com/NoobieDog/TPM-Sniffing" target="_blank">TPM-Sniffing</a> - Retrieving Bitlocker keys from the TPM using SPI, I2C or LPC communications requires an understanding of the specific protocol supported by the TPM chip, as well as the device's make and model.</li>
<li><a href="https://github.com/plerionhq/conditional-love/" target="_blank">conditional-love</a> - An AWS metadata enumeration tool.</li>
<li><a href="https://github.com/gatariee/gocheck" target="_blank">gocheck</a> -  GoCheck a blazingly fast™ alternative to Matterpreter's DefenderCheck which identifies the exact bytes that Windows Defender AV by feeding byte slices to MpCmdRun.exe</li>
<li><a href="https://github.com/ad0nis/ntlm_relay_gat" target="_blank">NTLM Relay Gat</a> - NTLM Relay Gat is a powerful tool designed to automate the exploitation of NTLM relays using ntlmrelayx.py from the Impacket tool suite. By leveraging the capabilities of ntlmrelayx.py, NTLM Relay Gat streamlines the process of exploiting NTLM relay vulnerabilities, offering a range of functionalities from listing SMB shares to executing commands on MSSQL databases.</li>
<li><a href="https://github.com/fin3ss3g0d/NativeThreadpool" target="_blank">Native Threadpool</a> -  Work, timer, and wait callback example using solely Native Windows APIs.</li>
<li><a href="https://github.com/WithSecureLabs/lolcerts" target="_blank">LoLCerts</a> -  A repository of code signing certificates known to have been leaked or stolen, then abused by threat actors</li>
<li><a href="https://br0k3nlab.com/LoFP/" target="_blank">Living off the False Positive!</a> - Living off the False Positive is an autogenerated collection of false positives sourced from some of the most popular rule sets. The information is categorized along with ATT&amp;CK techniques, rule source, and data source. Entries include details from related rules along with their description and detection logic. See the blog post <a href="https://br0k3nlab.com/posts/2024/02/introducing-lofp/" target="_blank">Introducing LoFP</a> for more info.</li>
<li><a href="https://github.com/iamagarre/BadExclusionsNWBO" target="_blank">BadExclusionsNWBO</a> - BadExclusionsNWBO is an evolution from BadExclusions to identify folder custom or undocumented exclusions on AV/EDR. An evolution of <a href="https://github.com/iamagarre/BadExclusions" target="_blank">BadExclusions</a>.</li>
<li><a href="https://github.com/SpiralBL0CK/Remote-buffer-overflow-over-wifi_stack-in-wpa_supplicant-binary-in-android-11-platform-samsung-a20e" target="_blank">Remote-buffer-overflow-over-wifi_stack-in-wpa_supplicant-binary-in-android-11-platform-samsung-a20e</a> - Remote buffer overflow over wifi_stack in wpa_supplicant binary in android 11, platform:samsung a20e, stock options so like works out of the box.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/anderspitman/awesome-tunneling" target="_blank">awesome-tunneling</a> -  List of ngrok alternatives and other ngrok-like tunneling software and services. Focus on self-hosting.</li>
<li><a href="https://github.com/leandrofroes/gftrace" target="_blank">gftrace</a> - A command line Windows API tracing tool for Golang binaries.</li>
<li><a href="https://github.com/spyr0-sec/AutomatedBadLab" target="_blank">AutomatedBadLab</a> - Scripts to provision vulnerable and testing environments using AutomatedLab.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 425 (+0)</p>
<p>Blogs monitored: 368 (+2)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
