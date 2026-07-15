Title: Last Week in Security (LWiS) - 2024-01-10
Date: 2024-01-10 15:35
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-01-10
Author: Erik
Summary: QR phishing (<a href="https://twitter.com/pfiatde" target="_blank">@pfiatde</a>), SOCKS as C2 via SSH on Windows (<a href="https://twitter.com/n00py1" target="_blank">@n00py1</a>), Google Account takeover with persistence (<a href="https://twitter.com/e11i0t_" target="_blank">@e11i0t_</a>), Bitwarden access without password (<a href="https://twitter.com/redteampt" target="_blank">@RedTeamPT</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-01-01 to 2024-01-10.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><p><a href="https://www.vice.com/en/article/bvjba8/this-ai-chatbot-is-trained-to-jailbreak-other-chatbots" target="_blank">This AI Chatbot is Trained to Jailbreak Other Chatbots</a>. When the AIs fight, humans win?</p>
</li>
<li><p>Twitter Hacks</p>
<blockquote>
<ul>
<li><a href="https://www.darkreading.com/cyberattacks-data-breaches/mandiant-s-x-twitter-account-hacked-to-promote-crypto-scam" target="_blank">Mandiant's X (Twitter) Account Hacked to Promote Crypto Scam</a></li>
<li><a href="https://www.theguardian.com/technology/2024/jan/09/sec-twitter-account-hacked-bitcoin-etf-not-approved" target="_blank">SEC says 'compromised' account to blame for tweet approving Bitcoin ETF</a></li>
</ul>
</blockquote>
</li>
<li><p><a href="https://www.cloudsek.com/blog/compromising-google-accounts-malwares-exploiting-undocumented-oauth2-functionality-for-session-hijacking" target="_blank">Compromising Google Accounts: Malwares Exploiting Undocumented OAuth2 Functionality for session hijacking</a>. And you thought Microsoft primary refresh tokens were powerful...</p>
</li>
<li><p><a href="https://www.scmagazine.com/news/npm-registry-prank-leaves-developers-unable-to-unpublish-packages" target="_blank">NPM registry prank leaves developers unable to unpublish packages</a>. A package that depended on every package on npm eventually got a circular dependency going and could not be removed. This also caused all public packages to be unable to be removed for a while.</p>
</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://objective-see.org/blog/blog_0x77.html" target="_blank">The Mac Malware of 2023 👾</a> - A technical deep dive into every new macOS malware specimen of 2023.</li>
<li><a href="https://rosesecurityresearch.com/crafting-malicious-pluggable-authentication-modules-for-persistence-privilege-escalation-and-lateral-movement" target="_blank">Crafting Malicious Pluggable Authentication Modules for Persistence, Privilege Escalation, and Lateral Movement</a> - How PAM (Pluggable Authentication Modules) can be harnessed to create malicious binaries for capturing credentials to use in persistence, privilege escalation, and lateral movement.</li>
<li><a href="https://nullg0re.com/2024/01/entra-id-connect-arbitrary-password-overwrite/" target="_blank">Entra ID Connect Arbitrary Password Overwrite</a> - Did you compromise the AADConnect Server and want to pivot to Azure without having to crack NT hashes? Overwrite any users NT hash with an attacker-controlled value and give yourself access to the organizations Azure subscription as the compromised user.</li>
<li><a href="https://trufflesecurity.com/blog/research-uncovers-aws-account-numbers-hidden-in-access-keys/" target="_blank">Research Uncovers AWS Account Numbers Hidden in Access Keys</a> - Some recent updates to trufflehog because of "...simple base-32 decoding and bit shifting can transform any AWS access key credential type into the corresponding account number."</li>
<li><a href="https://www.netspi.com/blog/technical/cloud-penetration-testing/automating-managed-identity-token-extraction-in-azure-container-registries/" target="_blank">Automating Managed Identity Token Extraction in Azure Container Registries</a> - Azure Container Registries (ACRs) can have attached Managed Identities and you can create malicious tasks in the ACR that generate and export tokens for the Managed Identities. New function added to <a href="https://github.com/NetSPI/MicroBurst" target="_blank">MicroBurst</a>.</li>
<li><a href="https://red.0xbad53c.com/red-team-operations/azure-and-o365/prt-abuse-from-userland-with-cobalt-strike/" target="_blank">PRT Abuse from Userland with Cobalt Strike</a> - How to acquire an Azure AD Single Sign-On session from a non-privileged user session on a victim host. The token is later used to enumerate Azure AD via ROADTools.</li>
<li><a href="https://badoption.eu/blog/2024/01/08/mobilephish.html" target="_blank">Phishing mobile devices, with DeviceCode phishing and QR codes</a>. Get yourself some Primary-Refresh-Tokens and plunder the GraphAPI.</li>
<li><a href="https://www.synacktiv.com/en/publications/exploring-counter-strike-global-offensive-attack-surface" target="_blank">Exploring Counter-Strike: Global Offensive Attack Surface</a>. Good exploit development content. Disappointing vulnerability management by Valve.</li>
<li><a href="https://www.n00py.io/2024/01/the-socks-we-have-at-home/" target="_blank">The SOCKS We Have at Home</a>. As EDR gets better "C2s" that are just network bridges are becoming more popular.</li>
<li><a href="https://rastamouse.me/safehandle-vs-intptr/" target="_blank">SafeHandle vs IntPtr</a>. How safe are your C# handles?</li>
<li><a href="https://posts.specterops.io/cypher-queries-in-bloodhound-enterprise-c7221a0d4bb3" target="_blank">Cypher Queries in BloodHound Enterprise</a>. Don't worry, it applies to open source BloodHound too.</li>
<li><a href="https://blog.redteam-pentesting.de/2024/bitwarden-heist/" target="_blank">Bitwarden Heist - How to Break Into Password Vaults Without Using Passwords</a>. If Windows Hello was enabled (fixed in October 2023) for Bitwarden, DPAPI could be used to extract a key that would unlock the vault without any user authentication or biometric prompts.</li>
<li><a href="https://mrbruh.com/chattr/" target="_blank">How I pwned half of America's fast food chains, simultaneously.</a>. To be fair it was the AI hiring chat bots/backend for a bunch of fast food chains, but still.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/msd0pe-1/cve-maker" target="_blank">CVE-MAKER</a> -  Tool to find CVEs and Exploits. It's a CLI.</li>
<li><a href="https://github.com/dmcxblue/SharpGhostTask" target="_blank">SharpGhostTask</a> -  A C# port from Invoke-GhostTask.</li>
<li><a href="https://github.com/blackarrowsec/Handly" target="_blank">Handly</a> -  Abuse leaked token handles. Token handles in MSSQL's process (sqlservr.exe) can be abused to change security context and escalate privileges both locally and in the domain.</li>
<li><a href="https://github.com/MegaManSec/SSH-Snake" target="_blank">SSH-Snake</a> -  A self-propagating, self-replicating, file-less script that automates the post-exploitation task of SSH private key and host discovery.</li>
<li><a href="https://github.com/swarmsecurity/swarm" target="_blank">Swarm</a> -  Formerly known as axiom, swarm is the next generation of distributed cloud scanning and attack surface monitoring.</li>
<li><a href="https://github.com/BC-SECURITY/Moriarty" target="_blank">Moriarty</a> - Moriarty is a comprehensive .NET tool that extends the functionality of Watson and Sherlock, originally developed by @_RastaMouse. It is designed to enumerate missing KBs, detect various vulnerabilities, and suggest potential exploits for Privilege Escalation in Windows environments.</li>
<li><a href="https://github.com/kyleavery/pendulum" target="_blank">pendulum</a> - Linux Sleep Obfuscation.</li>
<li><a href="https://github.com/0xNslabs/CanaryTokenScanner" target="_blank">CanaryTokenScanner</a> - CanaryTokenScanner is a script designed to proactively identify Canary Tokens within office documents (docx, xlsx, pptx).</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://adnanthekhan.com/2023/12/20/one-supply-chain-attack-to-rule-them-all/" target="_blank">One Supply Chain Attack to Rule Them All</a> - How self-hosted runners + supply chain attack led to these bounty hunters pwning a ton of orgs. Dope write-up!</li>
<li><a href="https://github.com/dub-flow/sessionprobe" target="_blank">sessionprobe</a> -  A multi-threaded tool designed for penetration testing and bug bounty hunting. It evaluates user privileges in web applications by taking a session token and checking access across a list of URLs, highlighting potential authorization issues.</li>
<li><a href="https://github.com/nolze/msoffcrypto-tool" target="_blank">msoffcrypto-tool</a> -  Python tool and library for decrypting MS Office files with passwords or other keys.</li>
<li><a href="https://gitlab.com/gitlab-com/gl-security/threatmanagement/redteam/redteam-public/continuousmage" target="_blank">ContinuousMage</a> - Continuousmage is automated testing PoC for the Mythic framework.</li>
<li><a href="https://github.com/BishopFox/jsluice" target="_blank">jsluice</a> -  Extract URLs, paths, secrets, and other interesting bits from JavaScript.</li>
<li><a href="https://github.com/Ap3x/COFF-Loader" target="_blank">COFF-Loader</a> -  A reimplementation of Cobalt Strike's Beacon Object File (BOF) Loader.</li>
<li><a href="https://github.com/ipSlav/DirtyCLR" target="_blank">DirtyCLR</a> - An App Domain Manager Injection DLL PoC on steroids and it came with a <a href="https://ipslav.github.io/2023-12-12-let-me-manage-your-appdomain/" target="_blank">blog post</a>.</li>
<li><a href="https://github.com/hrvach/deskhop" target="_blank">deskhop</a> - Fast Desktop Switching Device.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 425 (+0)</p>
<p>Blogs monitored: 364 (+0)</p>
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
