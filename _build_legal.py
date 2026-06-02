"""Regenerate the 3 legal pages from a canonical English-neutral scaffold.

GDPR-friendly placeholder text with {{TOKENS}} for identity fields.
**Not legal advice.** Each stamp must be reviewed for jurisdiction
(EU GDPR / UK GDPR / CCPA / state-specific) by a lawyer or by
substituting Loopi's vetted legal templates from
.claude/project-templates/legal/ before launch.
"""
import pathlib

ROOT = pathlib.Path(__file__).parent


def shell(slug_token: str, label_token: str, intro: str, sections: list[tuple[str, str]]) -> str:
    """Build a minimal legal page with shared header/footer + content sections."""
    section_html = '\n'.join(
        f'''        <section class="mb-10">
          <h2 class="font-display text-ink text-2xl md:text-3xl mb-4">{title}</h2>
          <div class="text-muted leading-relaxed space-y-4">{body}</div>
        </section>'''
        for title, body in sections
    )
    return f"""<!DOCTYPE html>
<html lang="{{{{LANG}}}}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{{{{label_token}}}}} | {{{{BUSINESS_NAME}}}}</title>
  <meta name="description" content="{{{{{label_token}}}}} for {{{{BUSINESS_NAME}}}}.">
  <meta name="robots" content="noindex, follow">
  <link rel="canonical" href="https://www.{{{{DOMAIN}}}}/{{{{{slug_token}}}}}">
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" href="/favicon-512.png" type="image/png">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <meta name="theme-color" content="{{{{BRAND_COLOR}}}}">
  <link rel="stylesheet" href="/fonts/fonts.css">
  <link rel="stylesheet" href="/styles.css">
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ font-family: 'DM Sans', system-ui, sans-serif; color: #1A1A1A; background: #FFFFFF; line-height: 1.6; }}
    a {{ color: {{{{BRAND_COLOR}}}}; }}
    h2 + div p {{ margin-bottom: 0.75em; }}
    ul {{ list-style: disc; padding-left: 1.5rem; }}
    ul li {{ margin-bottom: 0.5rem; }}
  </style>
</head>
<body>

<!-- ============================================================
     LEGAL PAGE SCAFFOLD — NOT LEGAL ADVICE.
     Placeholder GDPR-style copy in English. Every stamp must be
     reviewed for jurisdiction (EU / UK / US state-specific / etc.)
     or replaced with Loopi's vetted legal templates from
     .claude/project-templates/legal/ before going live.
     ============================================================ -->

  <header class="bg-dark text-white pt-16 pb-12 px-6">
    <div class="max-w-3xl mx-auto">
      <a href="/" class="inline-flex items-center gap-2 text-white/70 hover:text-white text-sm mb-6 transition-colors">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg>
        Back to home
      </a>
      <h1 class="font-display text-4xl md:text-5xl leading-[1.15]">{{{{{label_token}}}}}</h1>
      <p class="text-white/60 text-sm mt-3">Last updated: {{{{YEAR}}}}</p>
    </div>
  </header>

  <main class="py-16 px-6">
    <div class="max-w-3xl mx-auto">
      <p class="text-muted text-lg leading-relaxed mb-12">{intro}</p>
{section_html}

      <section class="mt-16 pt-8 border-t border-gray-200">
        <h2 class="font-display text-ink text-xl mb-3">Contact</h2>
        <p class="text-muted">
          Questions about this {{{{{label_token}}}}}? Reach us at
          <a href="mailto:{{{{EMAIL}}}}" class="underline hover:no-underline">{{{{EMAIL}}}}</a>
          or call <a href="tel:{{{{PHONE_INTL}}}}" class="underline hover:no-underline">{{{{PHONE_DISPLAY}}}}</a>.
        </p>
        <p class="text-muted mt-3">
          {{{{BUSINESS_NAME}}}}<br>
          {{{{STREET}}}}<br>
          {{{{POSTAL}}}} {{{{CITY_PRIMARY}}}}<br>
          {{{{TRUST_2_TITLE}}}}: {{{{LICENSE_ID}}}}
        </p>
      </section>
    </div>
  </main>

  <footer class="bg-dark text-white/60 py-8 px-6 text-center text-xs">
    <div class="max-w-6xl mx-auto">
      <p>&copy; {{{{YEAR}}}} {{{{BUSINESS_NAME}}}}. {{{{COPYRIGHT_TAIL}}}}</p>
      <div class="mt-4 flex flex-wrap justify-center gap-x-6 gap-y-2">
        <a href="/{{{{LEGAL_PRIVACY_SLUG}}}}" class="hover:text-brand transition-colors">{{{{LEGAL_PRIVACY_LABEL}}}}</a>
        <a href="/{{{{LEGAL_TERMS_SLUG}}}}" class="hover:text-brand transition-colors">{{{{LEGAL_TERMS_LABEL}}}}</a>
        <a href="/{{{{LEGAL_COOKIE_SLUG}}}}" class="hover:text-brand transition-colors">{{{{LEGAL_COOKIE_LABEL}}}}</a>
      </div>
    </div>
  </footer>

</body>
</html>
"""


# --- PRIVACY POLICY ---
privacy = shell(
    slug_token='LEGAL_PRIVACY_SLUG',
    label_token='LEGAL_PRIVACY_LABEL',
    intro="This policy explains what personal data {{BUSINESS_NAME}} collects, why we collect it, and how we handle it. By using our website or requesting a quote, you agree to the practices described below.",
    sections=[
        ("Who we are",
         "<p>{{BUSINESS_NAME}} ({{TRUST_2_TITLE}} {{LICENSE_ID}}) is the data controller for any personal data processed in connection with our services. We're based at {{STREET}}, {{POSTAL}} {{CITY_PRIMARY}}.</p>"),
        ("What we collect",
         "<p>We collect the minimum information needed to respond to your inquiry and deliver our services:</p>"
         "<ul>"
         "<li><strong>Contact details</strong> you give us through the quote form, phone, email, or messaging: name, phone number, email, postal code, and the service you're asking about.</li>"
         "<li><strong>Service details</strong> you share when describing your project (address, photos you send, notes about the job).</li>"
         "<li><strong>Anonymous site analytics</strong> if you accept cookies: pages viewed, referrer, device type, approximate location by IP. We do not link this to your identity.</li>"
         "</ul>"),
        ("Why we use it",
         "<ul>"
         "<li>Respond to your quote request and schedule the visit.</li>"
         "<li>Complete the work you've hired us for and invoice you.</li>"
         "<li>Follow up with you after the job (warranty, future maintenance reminders) unless you opt out.</li>"
         "<li>Improve how the website performs (anonymized analytics only).</li>"
         "</ul>"
         "<p>We do not sell your data. We do not share it with third parties for marketing.</p>"),
        ("How long we keep it",
         "<p>Quote requests that don't become jobs: deleted within 12 months. Records of completed work and invoices: kept as long as required by tax law in our jurisdiction (typically 5–7 years), then deleted.</p>"),
        ("Who we share it with",
         "<p>We share data only when needed to deliver the service or comply with law:</p>"
         "<ul>"
         "<li>Our CRM and quote-management software (acts as a data processor under a signed agreement).</li>"
         "<li>Payment processors when you pay us by card or transfer.</li>"
         "<li>Our accountant or tax authorities, where required.</li>"
         "</ul>"
         "<p>If we ever need to share more, we'll ask first.</p>"),
        ("Your rights",
         "<p>You can ask us at any time to:</p>"
         "<ul>"
         "<li>See a copy of the personal data we hold about you.</li>"
         "<li>Correct anything that's wrong.</li>"
         "<li>Delete your data (subject to legal retention obligations on completed work).</li>"
         "<li>Opt out of any non-essential communication.</li>"
         "<li>Lodge a complaint with the relevant data protection authority in your country.</li>"
         "</ul>"
         "<p>Email <a href='mailto:{{EMAIL}}'>{{EMAIL}}</a> and we'll respond within 30 days.</p>"),
        ("Cookies",
         "<p>See our <a href='/{{LEGAL_COOKIE_SLUG}}'>{{LEGAL_COOKIE_LABEL}}</a> for details on which cookies we set and how to control them.</p>"),
        ("Changes",
         "<p>We update this policy when our practices change. The 'last updated' date above always reflects the most recent revision.</p>"),
    ],
)

# --- TERMS OF SERVICE ---
terms = shell(
    slug_token='LEGAL_TERMS_SLUG',
    label_token='LEGAL_TERMS_LABEL',
    intro="These terms apply when you hire {{BUSINESS_NAME}} for any service. By accepting a written quote from us, you agree to the terms below.",
    sections=[
        ("Quotes",
         "<p>Quotes are issued in writing after an on-site evaluation. They include scope of work, materials, labor, and a timeline. Quotes are valid for 30 days unless stated otherwise. Verbal estimates are not binding.</p>"),
        ("Acceptance and start",
         "<p>You accept a quote by replying in writing (email, SMS, signed paper) or by paying a deposit if one is requested. We schedule the start date after acceptance, subject to weather and material availability.</p>"),
        ("Scope changes",
         "<p>If you ask for changes during the job, or we discover something unexpected (hidden damage, rot, code violations), we'll stop, document the change, and give you a revised price in writing before continuing. You decide whether to approve the change.</p>"),
        ("Payment",
         "<p>Payment terms are stated on each quote. Standard terms: balance due on completion. Accepted methods: {{PAYMENT_METHODS}}. Larger jobs may be split into milestones (e.g., 30% deposit, 40% mid-job, 30% on completion).</p>"
         "<p>Late payments may accrue interest at the legal rate in our jurisdiction. We don't release final lien waivers until payment clears.</p>"),
        ("Warranty",
         "<p>Our workmanship is warranted for the period stated on the invoice (typically 12 months). Manufacturer warranties on materials are passed through to you. The warranty does not cover damage caused by misuse, neglect, weather events, third-party modifications, or normal wear and tear.</p>"),
        ("Liability",
         "<p>{{BUSINESS_NAME}} carries general liability and (where applicable) workers' compensation insurance. Our liability for any claim is capped at the total amount you paid us for the job in question. We are not liable for indirect, consequential, or incidental damages.</p>"),
        ("Cancellation",
         "<p>You can cancel before work starts at no charge. Once materials have been ordered or work begun, you remain liable for materials and the proportion of labor already performed. We can cancel if site conditions are unsafe or if you fail to pay a milestone, and you'll only be charged for work completed.</p>"),
        ("Disputes",
         "<p>If something's wrong, tell us first — we'd much rather fix it than fight about it. If we can't resolve it directly, the dispute is governed by the laws of our jurisdiction and decided by the courts where we're registered.</p>"),
    ],
)

# --- COOKIE POLICY ---
cookies = shell(
    slug_token='LEGAL_COOKIE_SLUG',
    label_token='LEGAL_COOKIE_LABEL',
    intro="This page explains what cookies and similar technologies we use on this website, what they do, and how you can control them.",
    sections=[
        ("What are cookies",
         "<p>Cookies are small text files that a website stores in your browser. They let the site remember things between visits (e.g., that you've already dismissed a banner) and help us understand how people use the site.</p>"),
        ("Cookies we use",
         "<p><strong>Strictly necessary (always on):</strong></p>"
         "<ul>"
         "<li><code>{{COOKIE_STORAGE_KEY}}</code> — remembers whether you accepted or declined non-essential cookies. Stored locally for 12 months.</li>"
         "</ul>"
         "<p><strong>Analytics (only if you accept):</strong></p>"
         "<ul>"
         "<li>Anonymous page-view tracking via our analytics provider. Records page URL, referrer, device type, approximate location by IP. Does not personally identify you. Cookies expire after 14 months.</li>"
         "</ul>"
         "<p><strong>Embedded forms and widgets:</strong></p>"
         "<ul>"
         "<li>The quote form on our site is hosted by a third party. When you load the form, that provider may set its own cookies to make the form work. We do not control those cookies — see the provider's policy for details.</li>"
         "</ul>"),
        ("How to control cookies",
         "<p>You can accept or decline non-essential cookies using the banner that appears the first time you visit. Your choice is remembered for 12 months. To change it, clear the <code>{{COOKIE_STORAGE_KEY}}</code> key in your browser's site data, then reload — the banner will reappear.</p>"
         "<p>You can also block or delete cookies entirely in your browser settings. The site will still work, but the banner will show every visit.</p>"),
        ("Do Not Track",
         "<p>If your browser sends a 'Do Not Track' signal, we treat that as a decline of non-essential cookies.</p>"),
        ("Changes",
         "<p>If we add new cookies or change how existing ones work, we'll update this page and ask for fresh consent through the banner.</p>"),
    ],
)


(ROOT / 'privatlivspolitik.html').write_text(privacy, encoding='utf-8')
(ROOT / 'handelsbetingelser.html').write_text(terms, encoding='utf-8')
(ROOT / 'cookie-politik.html').write_text(cookies, encoding='utf-8')
print('wrote privatlivspolitik.html  (-> {{LEGAL_PRIVACY_SLUG}}.html on stamp)')
print('wrote handelsbetingelser.html (-> {{LEGAL_TERMS_SLUG}}.html on stamp)')
print('wrote cookie-politik.html     (-> {{LEGAL_COOKIE_SLUG}}.html on stamp)')
