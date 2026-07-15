Title: Last Week in Security (LWiS) - 2024-03-04
Date: 2024-03-04 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-03-04
Author: Erik
Summary: macOS LPE (<a href="https://twitter.com/patch1t" target="_blank">@patch1t</a>), Ivanti backdoors (<a href="https://twitter.com/NVISO_Labs" target="_blank">@NVISO_Labs</a>), ESC14 (<a href="https://twitter.com/Jonas_B_K" target="_blank">@Jonas_B_K</a>), token theft (<a href="https://twitter.com/rootsecdev" target="_blank">@rootsecdev</a>), LSASS dumping (<a href="https://twitter.com/Octoberfest73" target="_blank">@Octoberfest73</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-02-26 to 2024-03-04.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.kali.org/blog/kali-linux-2024-1-release/" target="_blank">Kali Linux 2024.1 Release</a> - They fixed <a href="https://bugs.kali.org/view.php?id=8628" target="_blank">this crippling bug in dpkg</a>. <a href="https://ludus.cloud" target="_blank">Ludus</a> will ship with Kali 2024.1 in 1.2.1 (next release).</li>
<li><a href="https://binary.ninja/2024/02/28/4.0-dorsai.html" target="_blank">Binary Ninja 4.0: Dorsai</a> - The latest major update for the much loved reverse engineering tool.</li>
<li><a href="https://arstechnica.com/gadgets/2024/02/hp-wants-you-to-pay-up-to-36-month-to-rent-a-printer-that-it-monitors/" target="_blank">HP wants you to pay up to $36/month to rent a printer that it monitors</a> - Buy a black and white laser printer and never give another dollar to HP.</li>
<li><a href="https://therecord.media/merck-insurance-settlement-notpetya" target="_blank">Merck settles with insurers who denied $700 million NotPetya claim</a> - The "11th-hour" settlement leaves more questions, but it seems that Merck got some payout. New policies are sure to include language exempting "state-sponsored" attacks, which will make attribution a multi-million dollar business.</li>
<li><a href="https://www.zetter-zeroday.com/nevada-ag-asks-court-to-ban-meta-from-providing-end-to-end-encryption-to-minors/?ref=zero-day-newsletter" target="_blank">Nevada AG Asks Court to Ban Meta from Providing End-to-End Encryption to Minors</a> - First they come saying, "won't you think of the children," then...</li>
<li><a href="https://computer.rip/" target="_blank">2024-03-01 listening in on the neighborhood</a> - The ShotSpotter/SoundThinking location database has been leaked. Why do you care? These government controlled microphones have been used to record conversations that were then <a href="https://casetext.com/case/people-v-johnson-5116" target="_blank">used in a court case</a>.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.atredis.com/blog/2024/2/9/scrutinizing-the-scrutinizer" target="_blank">Scrutinizing the Scrutinizer</a> - What's more fun than getting an unauthenticated root shell on a network monitoring appliance?</li>
<li><a href="https://code-white.com/blog/leaking-objrefs-to-exploit-http-dotnet-remoting/" target="_blank">Leaking ObjRefs to Exploit HTTP .NET Remoting</a> - You've heard of PS remoting (aka WinRM) but what about .NET Remoting? Turns out it can provide remote code execution. Sad that Microsoft didn't assign a CVE or give code white any credit, despite clearly patching this issue based on their report.</li>
<li><a href="https://jhftss.github.io/CVE-2023-42942-xpcroleaccountd-Root-Privilege-Escalation/" target="_blank">CVE-2023-42942: xpcroleaccountd Root Privilege Escalation</a> - A nice privesc for macOS.</li>
<li><a href="https://blog.nviso.eu/2024/03/01/covert-tls-n-day-backdoors-sparkcockpit-sparktar/" target="_blank">Covert TLS n-day backdoors: SparkCockpit &amp; SparkTar</a> - Some actors used the Ivanti Pluse Secure exploits to lay down some pretty sophisiticated backdoors.</li>
<li><a href="https://pentestlab.blog/2024/03/04/persistence-visual-studio-code-extensions/" target="_blank">Persistence - Visual Studio Code Extensions</a> - VSCode is found on nearly every developer's machine. This post presents a few options for how to use it for persistence.</li>
<li><a href="https://drive.google.com/file/d/1pYUm6XnKbe-TJsQt2H0jw9VbT_dO6Skk/view" target="_blank">[PDF] ComPromptMized: Unleashing Zero-click Worms that Target GenAI-Powered Applications</a> - An interesting approach to targeting retrieval-augmented generation (RAG) systems.</li>
<li><a href="https://posts.specterops.io/adcs-esc14-abuse-technique-333a004dc2b9" target="_blank">ADCS ESC14 Abuse Technique</a> - While not technically a new technique, its promotion to ESC14 will give it new prominence.</li>
<li><a href="https://trustedsec.com/blog/weaponization-of-token-theft-a-red-team-perspective" target="_blank">Weaponization of Token Theft - A Red Team Perspective</a> - Token theft isn't new, but this is a nice summary of a few techniques to leverage it.</li>
<li><a href="https://redsiege.com/blog/2024/03/dumping-lsass-like-its-2019/" target="_blank">Dumping LSASS Like it's 2019</a> - A theme of using "old and discarded" tooling to dump LSASS in 2024 against an EDR via Cobalt Strike BOFs.</li>
<li><a href="https://www.netspi.com/blog/technical/cloud-penetration-testing/extracting-sensitive-information-from-azure-batch-service/" target="_blank">Extracting Sensitive Information from the Azure Batch Service</a> - Azure Batch service can be fruitful depending on your permissions. Keep a look out for these! Defenders, restrict who has these permissions in your tenants.</li>
<li><a href="https://www.semperis.com/blog/meet-silver-saml/" target="_blank">Meet Silver SAML: Golden SAML in the Cloud</a> - "Any attacker that obtains the private key of an externally generated certificate can forge any SAML response they want and sign that response with the same private key that Entra ID holds. With this type of forged SAML response, the attacker can then access the application—as any user." Compromised cloud environment could get messy. This (for the moment) is likely a great option to Entra ID persistence.</li>
<li><a href="https://www.aon.com/en/insights/cyber-labs/duality-part-1" target="_blank">DUALITY: Advanced Red Team Persistence through Self-Reinfecting DLL Backdoors for Unyielding Control</a> - A lot to digest on this one. It's a long read. It's an interesting concept as "pesky" persistence. I have concerns on how loud it could be during red team ops. Code <a href="https://github.com/AonCyberLabs/DUALITY" target="_blank">here</a>.</li>
<li><a href="https://medium.com/@soufianehabti/unveiling-the-secrets-ssrf-adventures-in-microsofts-ai-playground-26c7872b32fc" target="_blank">SSRF в Microsoft Designer</a> - SSRF in Microsoft Designer.</li>
<li><a href="https://gatari.dev/posts/a-trip-down-memory-lane/" target="_blank">A Trip Down Memory Lane</a> - The frustration and walkthrough of this one stuck out. It really shows the thought process and frustrations of evading endpoint detection. And "...do your dev work on a VM with no internet access...". We agree! Use <a href="https://ludus.cloud/" target="_blank">Ludus</a>. The post drops a tool called <a href="https://github.com/gatariee/ldrgen" target="_blank">ldrgen</a> - Template-based generation of shellcode loaders.</li>
<li><a href="https://doubleagent.net/telecommunications/backdoor/gtp/2024/02/27/GTPDOOR-COVERT-TELCO-BACKDOOR" target="_blank">GTPDOOR - A novel backdoor tailored for covert access over the roaming exchange</a> - Some very stealth APT has to be upset with this post. Great find and RE work!</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/U53RW4R3/RKS" target="_blank">RKS</a> - A script to automate keystrokes through a graphical desktop program (<a href="https://github.com/skelsec/evilrdp" target="_blank">evilrdp</a> may be a better choice).</li>
<li><a href="https://github.com/Semperis/SilverSamlForger" target="_blank">SilverSamlForger</a> - Silver SAML Forger is C# tool that helps you create custom SAML responses. It can be used to implement the Silver SAML attack.</li>
<li><a href="https://github.com/projectdiscovery/dnsx/releases/tag/v1.2.0" target="_blank">dnsx 1.2.0</a> - This release adds the <cite>-recon</cite> flag which could eliminate/augment other tools in your recon pipeline.</li>
<li><a href="https://github.com/MultSec/MultCheck" target="_blank">MultCheck</a> - Identifies bad bytes from static analysis with any Anti-Virus scanner.</li>
<li><a href="https://github.com/Yeeb1/SharpLansweeperDecrypt" target="_blank">SharpLansweeperDecrypt</a> - Automatically extract and decrypt all configured scanning credentials of a Lansweeper instance.</li>
<li><a href="https://github.com/sensepost/mail-in-the-middle" target="_blank">mail-in-the-middle</a> - Typo squating + mail = shells. See the <a href="https://sensepost.com/blog/2024/mail-in-the-middle-a-tool-to-automate-spear-phishing-campaigns/" target="_blank">Mail in the Middle</a> post for more info.</li>
<li><a href="https://github.com/vysecurity/Nemesis-Download-Watcher/" target="_blank">Nemesis-Download-Watcher</a> - Watches the Downloads folder for any new files and inserts it into Nemesis for analysis.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/Ne0nd0g/winhttp" target="_blank">winhttp</a>  A library to make HTTP requests with the Windows winhttp API</li>
<li><a href="https://github.com/WhiteOakSecurity/GoAWSConsoleSpray" target="_blank">GoAWSConsoleSpray</a> -  Tool to spray AWS Console IAM Logins</li>
<li><a href="https://github.com/Devolutions/devolutions-gateway" target="_blank">Devolutions Gateway</a> - A blazing fast relay server adaptable to different protocols and desired levels of traffic inspection.</li>
<li><a href="https://github.com/DarkWolf-Labs/playbooks/blob/main/Android-Security-Research-Playbook.pdf" target="_blank">[PDF] Android-Security-Research-Playbook.pdf</a> - Darkwolf publishes their android research playbook</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 425 (+0)</p>
<p>Blogs monitored: 371 (+2)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
