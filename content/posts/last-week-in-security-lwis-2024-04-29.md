Title: Last Week in Security (LWiS) - 2024-04-29
Date: 2024-04-29 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-04-29
Author: Erik
Summary: AD Group abuse (<a href="https://twitter.com/decoder_it" target="_blank">@decoder_it</a>), NetNTLM leak attacks (<a href="https://twitter.com/PfiatDe" target="_blank">@pfiatde</a>), 'adversary flywheels' (<a href="https://twitter.com/whitehacksec" target="_blank">@WHITEHACKSEC</a>), Nemesis 1.0 (<a href="https://twitter.com/harmj0y" target="_blank">@harmj0y</a> + team) and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-04-22 to 2024-04-29.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://techcommunity.microsoft.com/t5/security-compliance-and-identity/trusted-signing-is-in-public-preview/ba-p/4103457" target="_blank">Trusted Signing is in Public Preview</a> - Code sign your payloads with Microsoft? Note that your company will need "3 years of tax history" to use the service.</li>
<li><a href="https://techcommunity.microsoft.com/t5/microsoft-365-blog/multi-tenant-organization-capabilities-now-available-in/ba-p/4122812" target="_blank">Multi-tenant organization capabilities now available in Microsoft 365</a> - This is AD forests for Entra ID with the ability to connect single tenants together. Let the games begin!</li>
<li><a href="https://www.hashicorp.com/blog/hashicorp-joins-ibm" target="_blank">HashiCorp joins IBM to accelerate multi-cloud automation</a> - HashiCorp joins IBM. This comes on the heels of their <a href="https://www.hashicorp.com/license-faq#aug-10-announcement" target="_blank">license changes for Terraform and Vault</a>. 🤔</li>
<li><a href="https://www.ftc.gov/news-events/news/press-releases/2023/05/ftc-says-ring-employees-illegally-surveilled-customers-failed-stop-hackers-taking-control-users" target="_blank">FTC Says Ring Employees Illegally Surveilled Customers, Failed to Stop Hackers from Taking Control of Users' Cameras</a> - The FTC charged Ring with privacy violations, including unauthorized employee access to customer videos and inadequate security measures, leading to a proposed order requiring Ring to improve privacy protocols and pay $5.8 million in refunds. Consider using <a href="https://www.home-assistant.io/" target="_blank">home assistant</a> and <a href="https://frigate.video/" target="_blank">Frigate NVR</a> to keep all your security camera footage local.</li>
<li><a href="https://www.ftc.gov/news-events/news/press-releases/2024/04/ftc-announces-rule-banning-noncompetes" target="_blank">FTC Announces Rule Banning Noncompetes</a> - This likely affects many technology workers in the US.</li>
<li><a href="https://social.coop/@Yhg1s/112332127058328855" target="_blank">Google Lays off the Python Team?</a> - It seems they are moving the Python team to Germany? Unclear what the motivations were for these actions.</li>
<li><a href="https://www.nytimes.com/2024/04/23/technology/general-motors-spying-driver-data-consent.html" target="_blank">How G.M. Tricked Millions of Drivers Into Being Spied On (Including Me)</a> - Another blatant privacy violation that will probably go unpunished.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://decoder.cloud/2024/04/24/hello-im-your-domain-admin-and-i-want-to-authenticate-against-you/" target="_blank">Hello: I'm your Domain Admin and I want to authenticate against you</a> - A method for exploiting default Distributed COM permissions on DCs to intercept and relay the authentication of users, leading to privilege escalation and RCE (maybe) by leveraging "SilverPotato."</li>
<li><a href="http://www.legacyy.xyz/defenseevasion/windows/2024/04/24/disabling-etw-ti-without-ppl.html" target="_blank">ETW-ByeBye: Disabling ETW-TI Without PPL</a> - A vulnerability that allows disabling ETW-TI (Event Tracing for Windows Threat Intelligence) logging without Protected Process Light (PPL) requirements, using SeDebug or SeTcb privileges on certain Windows versions. PoC code and detection guidance is provided. Note: this only works on Windows 10, Windows 11 patched this bug.</li>
<li><a href="https://medium.com/foxio/ja4t-tcp-fingerprinting-12fb7ce9cb5a" target="_blank">JA4T: TCP Fingerprinting</a> - JA4 scanner released. Certainly worth adding to your recon worfklow and automation.</li>
<li><a href="https://badoption.eu/blog/2024/04/25/netntlm.html" target="_blank">NetNTLM is still a thing?</a> - Yes. Yes it is. This post gives a good recap of how you can still relay NetNTLM via various methods. Details some less common techniques like leveraging HTTP.SYS for setting up a listener without admin privileges, bypassing the Windows firewall, and using SSH for port forwarding to relay. You aren't checking emails or doing day to day activities with a highly privileged account, right?</li>
<li><a href="https://5stars217.github.io/2024-04-23-adversaries-sometimes-compute-gradients/" target="_blank">Adversaries sometimes compute gradients. Other times, they rob you.</a> This blog post discusses the concept of an "adversary flywheel," which involves attackers using data science to adapt and optimize their methods based on defensive responses, enhancing their ability to exploit security vulnerabilities efficiently.</li>
<li><a href="https://medium.com/@tamirye94/not-the-access-you-asked-for-how-azure-storage-account-read-write-permissions-can-be-abused-75311103430f" target="_blank">Not the Access You Asked For: How Azure Storage Account Read/Write Permissions Can Be Abused for Privilege Escalation and Lateral Movement</a> This post discusses unexpected techniques that allow an Azure user with Storage Account permissions to abuse them for privilege escalation and lateral movement. Grab the tool: <a href="https://github.com/Tamirye/Find-SensitiveAzStorageAccounts" target="_blank">Find-SensitiveAzStorageAccounts</a>.</li>
<li><a href="https://trustedsec.com/blog/loading-dlls-reflections" target="_blank">Loading DLLs Reflections</a> - Simple article discussing reflective DLL loading to load a DLL into memory without it being written to disk.</li>
<li><a href="https://posts.specterops.io/nemesis-1-0-0-8c6b745dc7c5" target="_blank">Nemesis 1.0.0</a> - "...from host modeling, to a streamlined installation process, dashboard improvements, and more!"</li>
<li><a href="https://blog.2h0ng.wiki/2024/04/27/LogonUserW%20Hooking/" target="_blank">Offensive SaaS Security - Exfiltrating Cleartext Credentials via LogonUserW Hooking</a> - This post details a technique exploiting IAM providers like Azure AD, Okta, and OneLogin using LogonUserW hooking to capture cleartext credentials and insert backdoors in authentication flows.</li>
<li><a href="https://falconforce.nl/arbitrary-1-click-azure-tenant-takeover-via-ms-application/" target="_blank">Arbitrary 1-click Azure tenant takeover via MS application</a> - Blog post on how reply URLs in Azure Applications can be used as a vector for phishing. The impact of this can range from data leaks to complete tenant takeover; just by luring a victim into clicking on a link. Another disappointing bug bounty case unfortunately.</li>
<li><a href="https://github.com/FuzzySecurity/SAFACon-Vienna/blob/main/SAFA-LaunderingC2Traffic.pdf" target="_blank">Laundering C2 Traffic by FuzzySecurity</a> Good recap of using high-reputation services as your C2 channel.</li>
<li><a href="https://exploits.forsale/24h2-nt-exploit/" target="_blank">Exploiting the NT Kernel in 24H2: New Bugs in Old Code &amp; Side Channels Against KASLR</a> - The kernel address space layout randomization (KASLR) cat and mouse game heats up with a bypass for the new Windows 11 24H2 hardened kernel.</li>
<li><a href="https://www.synacktiv.com/en/publications/so-i-became-a-node-exploiting-bootstrap-tokens-in-azure-kubernetes-service" target="_blank">So I Became a Node: Exploiting Bootstrap Tokens in Azure Kubernetes Service</a> - What can you do if you retrieve a Kubernetes bootstrap token from an AKS pod? This post explore the bootstrap tokens, how they work, and how to exploit them.</li>
<li><a href="https://www.mdsec.co.uk/2024/04/cve-2024-21111-local-privilege-escalation-in-oracle-virtualbox/" target="_blank">CVE-2024-21111 - Local Privilege Escalation in Oracle VirtualBox</a> - An arbitrary file move vulnerability in the VirtualBox system service service can facilitate privilege escalation on a Windows host.</li>
<li><a href="https://jakewnuk.com/posts/how-to-crack-the-perfect-egg/" target="_blank">How to Crack the Perfect Egg</a> - Some great password cracking methodology.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/sarperavci/GoogleRecaptchaBypass" target="_blank">GoogleRecaptchaBypass</a> - Solve Google reCAPTCHA in less than 5 seconds! 🚀</li>
<li><a href="https://github.com/fin3ss3g0d/ASPJinjaObfuscator" target="_blank">ASPJinjaObfuscator</a> - Heavily obfuscated ASP web shell generation tool.</li>
<li><a href="https://github.com/FoxIO-LLC/ja4tscan" target="_blank">ja4tscan</a> - JA4TScan is an active TCP server fingerprinting tool.</li>
<li><a href="https://github.com/adam-maj/tiny-gpu" target="_blank">tiny-gpu</a> - A minimal GPU design in Verilog to learn how GPUs work from the ground up.</li>
<li><a href="https://github.com/nbaertsch/AutoAppDomainHijack" target="_blank">AutoAppDomainHijack</a> - Automated .NET AppDomain hijack payload generation.</li>
<li><a href="https://github.com/Kharos102/ReadWriteDriverSample" target="_blank">ReadWriteDriverSample</a> - Sample driver + user component to demonstrate writing into arbitrary process memory from Kernel via CR3 manipulation (opposed to the usual KeStackAttachProcess API).</li>
<li><a href="https://github.com/itaymigdal/PartyLoader" target="_blank">PartyLoader</a> - Threadless shellcode injection tool.</li>
<li><a href="https://github.com/exploits-forsale/24h2-nt-exploit" target="_blank">24h2-nt-exploit</a> - Exploit targeting NT kernel in 24H2 Windows Insider Preview.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/microsoft/ics-forensics-tools" target="_blank">ics-forensics-tools</a> - Microsoft ICSpector (ICS Forensics Tools framework) is an open-source forensics framework that enables the analysis of Industrial PLC metadata and project files.</li>
<li><a href="https://github.com/scottleyg/SecOpsSamples/tree/develop/EvidenceCollection" target="_blank">Evidence Collection Environment</a> - This environment is intended to be useful for when you have multiple investigators or external parties adding data for evaluation. Some key features (hopefully) implemented in this setup leverage the Azure Storage legal hold, Azure Storage analytics logging for validation of access by which parties, Azure Key Vault logging with the logs going to a Log Analytics workspace in the resource group.</li>
<li><a href="https://github.com/synacktiv/DLHell" target="_blank">DLHell</a> - Local &amp; remote Windows DLL Proxying.</li>
<li><a href="https://github.com/microsoft/MS-DOS" target="_blank">MS-DOS</a> - The original sources of MS-DOS 1.25, 2.0, and 4.0 for reference purposes.</li>
<li><a href="https://github.com/projectdiscovery/cdncheck" target="_blank">cdncheck</a> - A utility to detect various technology for a given IP address.</li>
<li><a href="https://github.com/xpn/CloudInject" target="_blank">CloudInject</a> - This is a simple tool which can be used to inject a DLL into third-party AD connectors to harvest credentials.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 426 (+0)</p>
<p>Blogs monitored: 379 (+3)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
