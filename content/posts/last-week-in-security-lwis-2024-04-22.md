Title: Last Week in Security (LWiS) - 2024-04-22
Date: 2024-04-22 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-04-22
Author: Erik
Summary: LSA Whisperer (<a href="https://twitter.com/mcbroom_evan" target="_blank">@mcbroom_evan</a>), VirtualBox LPE (<a href="https://twitter.com/mansk1es" target="_blank">@mansk1es</a>), Android Intent exploitation (<a href="https://twitter.com/suidpit" target="_blank">@suidpit</a>), MagicDot "rootkit" (<a href="https://twitter.com/oryair1999" target="_blank">@oryair1999</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-04-16 to 2024-04-22.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.microsoft.com/en-us/research/project/vasa-1/" target="_blank">VASA-1: Lifelike Audio-Driven Talking Faces Generated in Real Time</a> - Just when you thought you could trust the <a href="https://www.cnn.com/2024/02/04/asia/deepfake-cfo-scam-hong-kong-intl-hnk/index.html" target="_blank">CFO ordering you to transfer all that money via Zoom</a>...</li>
<li><a href="https://llama.meta.com/llama3/" target="_blank">Build the future of AI with Meta Llama 3</a> - The best "open source" (sort of) model yet. Local AI just got a big boost.</li>
<li><a href="https://security.googleblog.com/2024/04/find-my-device-network-security-privacy-protections.html" target="_blank">How we built the new Find My Device network with user security and privacy in mind</a> - Google enters the "Find My" crowdsourced device-locating network game with the similarly named "Find My Device" network. It support the standard which allows trackers to be detected by iOS devices (and vice-versa) so unwanted trackers will alert users.</li>
<li><a href="https://www.bleepingcomputer.com/news/security/github-comments-abused-to-push-malware-via-microsoft-repo-urls/" target="_blank">GitHub comments abused to push malware via Microsoft repo URLs</a> - The fact that GitHub will upload a file to a publically accessable URL during comment editing, actors don't need to publish comments to get files hosted under trusted projects URLs. If you're ok with giving your payload to Microsoft (GitHub), this is a pretty sneaky way to host it.</li>
<li><a href="https://openjsf.org/blog/openssf-openjs-alert-social-engineering-takeovers" target="_blank">Open Source Security (OpenSSF) and OpenJS Foundations Issue Alert for Social Engineering Takeovers of Open Source Projects</a> - Echos of the XZ backdoor are still being felt.</li>
<li><a href="https://tailscale.com/blog/sso-tax-cut" target="_blank">SSO tax, cut</a> - Tailscale is the best VPN solution there is (unsponsored opinion). Between this change and <a href="https://tailscale.com/kb/1230/tailnet-lock-whitepaper?q=key+lock" target="_blank">Tailnet lock</a>, they have eliminated all issues I had with their service. If you're a self-hosting true purist, there is still <a href="https://github.com/juanfont/headscale" target="_blank">headscale</a>.</li>
<li><a href="https://www.mitre.org/news-insights/news-release/mitre-response-cyber-attack-one-its-rd-networks" target="_blank">MITRE Response to Cyber Attack in One of Its R&amp;D Networks</a> - MITRE was hit with the Ivanti 0day. Good transparency on what took place. Additional details <a href="https://medium.com/mitre-engenuity/advanced-cyber-threats-impact-even-the-most-prepared-56444e980dc8" target="_blank">here</a>.</li>
<li><a href="https://www.lares.com/blog/an-introduction-to-the-canadian-program-for-cyber-security-certification-cpcsc/" target="_blank">An Introduction to the Canadian Program for Cyber Security Certification (CPCSC)</a> - Starting at the end of 2024, Canadian defense industry suppliers will need to be certified under the Canadian Program for Cyber Security Certification (CPCSC) to bid on certain government contracts, an initiative designed to enhance security measures within the nation's federal contracting processes.</li>
<li><a href="https://www.38north.org/2024/04/what-we-learned-inside-a-north-korean-internet-server-how-well-do-you-know-your-partners/" target="_blank">What We Learned Inside a North Korean Internet Server: How Well Do You Know Your Partners?</a> - A misconfigured North Korean internet server exposes the nation's outsourcing of animation work. Is your "IT partner" North Korea?</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.synacktiv.com/en/publications/ounedpy-exploiting-hidden-organizational-units-acl-attack-vectors-in-active-directory" target="_blank">ouned.py: Exploiting Hidden Organizational Units Acl Attack Vectors in Active Directory</a> - You know "GenericAll" but what other OU permissions can be abused in Active Directory? Read this post to learn about gPLink poisoning. <a href="https://github.com/synacktiv/OUned" target="_blank">OUned</a> is the tool.</li>
<li><a href="https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2023/CVE-2023-6345.html" target="_blank">CVE-2023-6345: Integer overflow in Skia MeshOp::onCombineIfPossible</a> - An intiger overflow in the Skia graphics library has been used to exploit Chrome. The fact that it would not appear in debug builds due to <cite>assert</cite> calls that are not compiled with release builds is interesting. Make sure you are fuzzing release binaries!</li>
<li><a href="https://www.shielder.com/blog/2024/04/element-android-cve-2024-26131-cve-2024-26132-never-take-intents-from-strangers/" target="_blank">Element Android CVE-2024-26131, CVE-2024-26132 - Never Take Intents From Strangers</a> - A very in-depth post on Android app Intents and how they can be exploited, especially in "high security" apps like chat or cyptocurrency apps.</li>
<li><a href="https://labs.nettitude.com/blog/cve-2024-20356-jailbreaking-a-cisco-appliance-to-run-doom/" target="_blank">CVE-2024-20356: Jailbreaking a Cisco appliance to run DOOM</a> - The out-of-band management chips on enterprise servers are nutorious for being vulnerable. Cisco's is no exception.</li>
<li><a href="https://posts.specterops.io/lsa-whisperer-20874277ea3b" target="_blank">LSA Whisperer</a> - Some seriously indepth research into the local security authority (LSA) of Windows which leads to all kinds of functionality. My favorite is the possible use of <cite>CacheLogon</cite> to cache a specific NT hash into an active logon session which will allow for stable Pass-the-hash without having to patch LSASS memory (but will require injection into LSASS). I can only imagine the amount of reverse-engineering it took to get to the <a href="https://github.com/EvanMcBroom/lsa-whisperer" target="_blank">lsa-whisperer</a>.</li>
<li><a href="https://www.guidepointsecurity.com/blog/a-crash-course-in-hardware-hacking-methodology-the-ones-and-zeros/" target="_blank">A Crash Course in Hardware Hacking Methodology: The Ones and Zeros</a> - A good primer on IoT hacking.</li>
<li><a href="https://blog.quarkslab.com/passbolt-a-bold-use-of-haveibeenpwned.html" target="_blank">Passbolt: a bold use of HaveIBeenPwned</a> - Passbolt is a password manager that uses the HaveIBeenPwned API to check if a password has been compromised. This post goes into the details of how they implemented it.</li>
<li><a href="https://www.sprocketsecurity.com/resources/patch-diffing-cve-2024-3400-from-a-palo-alto-ngfw-marketplace-ami" target="_blank">Patch Diffing CVE-2024-3400 from a Palo Alto NGFW Marketplace AMI</a> - Saving some of the commands here for future use. Those AWS AMIs can certainly come in handy.</li>
<li><a href="https://zeyadazima.com/exploit%20development/ropdecoder/" target="_blank">ROPGadget: Writing a ROPDecoder</a> - This post discusses creating a ROPDecoder from scratch, detailing the selection and use of ROP gadgets to encode and decode shellcode, and automating the process to handle bad characters effectively in exploit dev.</li>
<li><a href="https://googleprojectzero.blogspot.com/2024/04/the-windows-registry-adventure-1.html" target="_blank">The Windows Registry Adventure #1: Introduction and research results</a> - Wild. Mateusz Jurczyk of Google Project Zero audited the Windows Registry for local privilege escalation bugs over 20 months, identifying multiple vulnerabilities now fixed as 44 CVEs by Microsoft, utilizing methods from fuzzing to manual review in an extensive security research effort.</li>
<li><a href="https://www.datadoghq.com/state-of-devsecops/" target="_blank">State of DevSecOps</a> - Datadog's State of DevSecOps report is out. TLDR - Java/JS account for tons of issues, automated security scanners are just noise, the industry sucks at prioritizing what to fix, manual cloud deployments (no IaC) is still very common, and more.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/mansk1es/CVE-2024-21111" target="_blank">CVE-2024-21111</a> - Oracle VirtualBox Elevation of Privilege (Local Privilege Escalation) Vulnerability.</li>
<li><a href="https://github.com/EvanMcBroom/lsa-whisperer" target="_blank">lsa-whisperer</a> - Tools for interacting with authentication packages using their individual message protocols.</li>
<li><a href="https://github.com/floesen/KExecDD" target="_blank">KExecDD</a> - Admin to Kernel code execution using the KSecDD driver.</li>
<li><a href="https://github.com/Permiso-io-tools/CloudConsoleCartographer" target="_blank">CloudConsoleCartographer</a> - Released at Black Hat Asia on April 18, 2024, Cloud Console Cartographer is a framework for condensing groupings of cloud events (e.g. CloudTrail logs) and mapping them to the original user input actions in the management console UI for simplified analysis and explainability.</li>
<li><a href="https://github.com/marco-liberale/PasteBomb" target="_blank">PasteBomb</a> - PasteBomb C2-less RAT. The creator of this project is only 13 years old. Impressive! Great work.</li>
<li><a href="https://github.com/boostsecurityio/poutine/" target="_blank">poutine</a> - poutine is a security scanner that detects misconfigurations and vulnerabilities in the build pipelines of a repository. It supports parsing CI workflows from GitHub Actions and Gitlab CI/CD.</li>
<li><a href="https://github.com/k4nfr3/panos-scanner" target="_blank">panos-scanner</a> - Determine the Palo Alto PAN-OS software version of a remote GlobalProtect portal or management interface.</li>
<li><a href="https://github.com/Meowmycks/LetMeowIn" target="_blank">LetMeowIn</a> - A sophisticated, covert Windows-based credential dumper using C++ and MASM x64.</li>
<li><a href="https://github.com/SafeBreach-Labs/MagicDot" target="_blank">MagicDot</a> - A set of rootkit-like abilities for unprivileged users, and vulnerabilities based on the DOT-to-NT path conversion known issue.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/Moopinger/smugglefuzz" target="_blank">smugglefuzz</a> - A rapid HTTP downgrade smuggling scanner written in Go.</li>
<li><a href="https://github.com/spectralops/netz" target="_blank">netz</a> - Discover internet-wide misconfigurations while drinking coffee.</li>
<li><a href="https://github.com/padok-team/cognito-scanner" target="_blank">cognito-scanner</a> - A simple script which implements different Cognito attacks such as Account Oracle or Privilege Escalation.</li>
<li><a href="https://securitylabs.datadoghq.com/articles/amplified-exposure-how-aws-flaws-made-amplify-iam-roles-vulnerable-to-takeover/" target="_blank">Amplified exposure: How AWS flaws made Amplify IAM roles vulnerable to takeover</a> - A deep dive into AWS Amplify and how it can be abused.</li>
<li><a href="https://www.elastic.co/blog/elastic-universal-profiling-agent-open-source" target="_blank">Elastic Universal Profiling agent, a continuous profiling solution, is now open source</a> - Elastic has open sourced their profiling agent.</li>
<li><a href="https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/active-directory-hardening-series-part-4-enforcing-aes-for/ba-p/4114965" target="_blank">Active Directory Hardening Series - Part 4 - Enforcing AES for Kerberos</a> - Part 4 of the Active Directory Hardening Series.</li>
<li><a href="https://m4lwhere.medium.com/the-ultimate-guide-for-bloodhound-community-edition-bhce-80b574595acf" target="_blank">The Ultimate Guide for BloodHound Community Edition (BHCE)</a> - A guide to BloodHound Community Edition. Also gives the background of the project for those that are new to Bloodhound in general.</li>
<li><a href="https://boostsecurityio.github.io/lotp/" target="_blank">Living Off the Pipeline</a> - "....to inventory how development tools (typically CLIs), commonly used in CI/CD pipelines, have lesser-known RCE-By-Design features ("foot guns"), or more generally, can be used to achieve arbitrary code execution by running on untrusted code changes or following a workflow injection. "</li>
<li><a href="https://github.com/secureworks/BAADTokenBroker" target="_blank">BAADTokenBroker</a> post-exploitation tool designed to leverage device-stored keys (Device key, Transport key etc..) to authenticate to Microsoft Entra ID.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 426 (+1)</p>
<p>Blogs monitored: 376 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
