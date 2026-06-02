"""Regenerate the 5 service subpages from one canonical English-neutral scaffold.

Each subpage is identical in structure and copy — only the SERVICE_N index
shifts (1..5), so the same scaffold gets rendered 5 times. The body copy is
deliberately neutral and 'fillable': sections read coherently as-is, but each
section is a clear slot for client-specific rewriting during stamping.

After running this script, run `_build_legal.py` for the legal scaffolds,
then stamp via `stamp.py client.json out-folder/`.

Run once after editing the scaffold below.
"""
import pathlib

ROOT = pathlib.Path(__file__).parent

# Map: source filename (Danish) -> SERVICE_N index, kept so existing stamping
# rename logic (in stamp.py) still works. Once stamped, the file becomes
# {SERVICE_N_SLUG}.html.
SUBPAGES = {
    'toemrerarbejde.html':  1,
    'renovering.html':       2,
    'tagprojekter.html':     3,
    'traeterrasser.html':    4,
    'vinduer-og-doere.html': 5,
}

# The "other 4" services to surface in Related Services per subpage
RELATED_FOR = {
    1: (2, 3, 4),
    2: (1, 3, 5),
    3: (1, 2, 4),
    4: (2, 3, 5),
    5: (1, 2, 3),
}


def page(n: int) -> str:
    """Return a full HTML subpage pinned to SERVICE_N."""
    a, b, c = RELATED_FOR[n]
    return f"""<!DOCTYPE html>
<html lang="{{{{LANG}}}}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{{{SERVICE_{n}_NAME}}}} in {{{{PRIMARY_REGION}}}} | {{{{BUSINESS_NAME}}}}</title>
  <meta name="description" content="{{{{SERVICE_{n}_NAME}}}} from {{{{BUSINESS_NAME}}}}, serving {{{{PRIMARY_REGION}}}}. {{{{SERVICE_{n}_BLURB}}}} Call {{{{PHONE_DISPLAY}}}}.">
  <meta name="robots" content="index, follow">
  <link rel="preload" as="image" href="/brand-assets/subpage-{n}.webp" fetchpriority="high">
  <link rel="canonical" href="https://www.{{{{DOMAIN}}}}/{{{{SERVICE_{n}_SLUG}}}}">

  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.{{{{DOMAIN}}}}/{{{{SERVICE_{n}_SLUG}}}}">
  <meta property="og:title" content="{{{{SERVICE_{n}_NAME}}}} in {{{{PRIMARY_REGION}}}} | {{{{BUSINESS_NAME}}}}">
  <meta property="og:description" content="{{{{SERVICE_{n}_BLURB}}}}">
  <meta property="og:image" content="https://www.{{{{DOMAIN}}}}/brand-assets/og-image.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{{{{SERVICE_{n}_NAME}}}} in {{{{PRIMARY_REGION}}}}">
  <meta name="twitter:description" content="{{{{SERVICE_{n}_BLURB}}}}">
  <meta name="twitter:image" content="https://www.{{{{DOMAIN}}}}/brand-assets/og-image.jpg">

  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" href="/favicon-512.png" type="image/png">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <meta name="theme-color" content="{{{{BRAND_COLOR}}}}">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.{{{{DOMAIN}}}}/" }},
      {{ "@type": "ListItem", "position": 2, "name": "{{{{SERVICE_{n}_NAME}}}}", "item": "https://www.{{{{DOMAIN}}}}/{{{{SERVICE_{n}_SLUG}}}}" }}
    ]
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "{{{{SERVICE_{n}_NAME}}}}",
    "serviceType": "{{{{SERVICE_{n}_TYPE}}}}",
    "description": "{{{{SERVICE_{n}_SCHEMA_DESC}}}}",
    "url": "https://www.{{{{DOMAIN}}}}/{{{{SERVICE_{n}_SLUG}}}}",
    "provider": {{ "@id": "https://www.{{{{DOMAIN}}}}/#business" }},
    "areaServed": [
      {{ "@type": "City", "name": "{{{{CITY_1}}}}" }},
      {{ "@type": "City", "name": "{{{{CITY_2}}}}" }},
      {{ "@type": "City", "name": "{{{{CITY_3}}}}" }},
      {{ "@type": "City", "name": "{{{{CITY_4}}}}" }},
      {{ "@type": "City", "name": "{{{{CITY_5}}}}" }},
      {{ "@type": "AdministrativeArea", "name": "{{{{PRIMARY_REGION}}}}" }}
    ],
    "offers": {{
      "@type": "Offer",
      "availability": "https://schema.org/InStock",
      "priceSpecification": {{
        "@type": "PriceSpecification",
        "priceCurrency": "{{{{CURRENCY}}}}",
        "description": "{{{{TRUST_3_TITLE}}}} after on-site evaluation. Free quotes."
      }}
    }}
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{ "@type": "Question", "name": "{{{{SUBPAGE_{n}_FAQ_1_Q}}}}", "acceptedAnswer": {{ "@type": "Answer", "text": "{{{{SUBPAGE_{n}_FAQ_1_A}}}}" }} }},
      {{ "@type": "Question", "name": "{{{{SUBPAGE_{n}_FAQ_2_Q}}}}", "acceptedAnswer": {{ "@type": "Answer", "text": "{{{{SUBPAGE_{n}_FAQ_2_A}}}}" }} }},
      {{ "@type": "Question", "name": "{{{{SUBPAGE_{n}_FAQ_3_Q}}}}", "acceptedAnswer": {{ "@type": "Answer", "text": "{{{{SUBPAGE_{n}_FAQ_3_A}}}}" }} }},
      {{ "@type": "Question", "name": "{{{{SUBPAGE_{n}_FAQ_4_Q}}}}", "acceptedAnswer": {{ "@type": "Answer", "text": "{{{{SUBPAGE_{n}_FAQ_4_A}}}}" }} }}
    ]
  }}
  </script>

  <link rel="stylesheet" href="/fonts/fonts.css">
  <link rel="stylesheet" href="/styles.css">

  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ font-family: 'DM Sans', system-ui, sans-serif; color: #1A1A1A; background: #FFFFFF; }}
    .price-card {{ background: rgba(255, 250, 245, 0.6); border: 1px solid rgba(0, 0, 0, 0.06); }}
    .faq-item {{ border-bottom: 1px solid rgba(26, 26, 26, 0.08); }}
    .faq-item:last-child {{ border-bottom: none; }}
    .faq-toggle {{ cursor: pointer; }}
    .faq-answer {{ max-height: 0; overflow: hidden; transition: max-height 0.3s ease; }}
    .faq-answer.open {{ max-height: 800px; }}
    .faq-chevron {{ transition: transform 0.3s ease; }}
    .faq-item.open .faq-chevron {{ transform: rotate(180deg); }}
  </style>
</head>
<body>

  <!-- ============================================================
       SUBPAGE SCAFFOLD — service deep-dive page
       Pinned to SERVICE_{n}. Body content is industry-neutral
       English. Rewrite per client during stamping so the copy
       reflects their actual services, market, and voice.
       ============================================================ -->

  <!-- NAV -->
  <nav class="nav-bar fixed top-0 left-0 w-full z-50 bg-transparent">
    <div class="max-w-7xl mx-auto px-6 lg:px-8 flex items-center justify-between h-20">
      <a href="/" class="nav-logo flex items-center">
        <img src="/brand-assets/logo-280.webp" alt="{{{{BUSINESS_NAME}}}} logo" width="280" height="280" class="w-auto" style="height: 140px; margin: -50px 0;">
      </a>
      <div class="hidden lg:flex items-center gap-8">
        <a href="/#om-os" class="nav-link text-white/80 text-sm font-medium tracking-wide uppercase hover:text-white transition-colors duration-200">{{{{SECTION_ABOUT}}}}</a>
        <div class="nav-dropdown relative">
          <a href="/#ydelser" class="nav-link inline-flex items-center gap-1 text-white/80 text-sm font-medium tracking-wide uppercase hover:text-white transition-colors duration-200">
            {{{{SECTION_SERVICES}}}}
            <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>
          </a>
          <div class="nav-dropdown-panel absolute top-full left-1/2 pt-4 w-60">
            <div class="bg-white rounded-xl shadow-2xl border border-gray-100 py-2 overflow-hidden">
              <a href="/#ydelser" class="block px-5 py-3 text-sm font-medium tracking-wide uppercase text-ink hover:bg-cream transition-colors duration-200">{{{{NAV_ALL_SERVICES}}}}</a>
              <div class="border-t border-gray-100 my-1"></div>
              <a href="/{{{{SERVICE_1_SLUG}}}}" class="block px-5 py-3 text-sm font-medium tracking-wide uppercase text-ink hover:bg-cream transition-colors duration-200">{{{{SERVICE_1_NAME}}}}</a>
              <a href="/{{{{SERVICE_2_SLUG}}}}" class="block px-5 py-3 text-sm font-medium tracking-wide uppercase text-ink hover:bg-cream transition-colors duration-200">{{{{SERVICE_2_NAME}}}}</a>
              <a href="/{{{{SERVICE_3_SLUG}}}}" class="block px-5 py-3 text-sm font-medium tracking-wide uppercase text-ink hover:bg-cream transition-colors duration-200">{{{{SERVICE_3_NAME}}}}</a>
              <a href="/{{{{SERVICE_4_SLUG}}}}" class="block px-5 py-3 text-sm font-medium tracking-wide uppercase text-ink hover:bg-cream transition-colors duration-200">{{{{SERVICE_4_NAME}}}}</a>
              <a href="/{{{{SERVICE_5_SLUG}}}}" class="block px-5 py-3 text-sm font-medium tracking-wide uppercase text-ink hover:bg-cream transition-colors duration-200">{{{{SERVICE_5_NAME}}}}</a>
            </div>
          </div>
        </div>
        <a href="/#proces" class="nav-link text-white/80 text-sm font-medium tracking-wide uppercase hover:text-white transition-colors duration-200">{{{{NAV_PROCESS}}}}</a>
        <a href="/#galleri" class="nav-link text-white/80 text-sm font-medium tracking-wide uppercase hover:text-white transition-colors duration-200">{{{{SECTION_GALLERY}}}}</a>
        <a href="/#faq" class="nav-link text-white/80 text-sm font-medium tracking-wide uppercase hover:text-white transition-colors duration-200">{{{{NAV_FAQ}}}}</a>
        <div class="flex items-center gap-2">
          <a href="#" data-quote-trigger class="btn-primary inline-block bg-brand text-white font-bold text-sm px-8 py-4 rounded-lg tracking-wide uppercase">{{{{CTA_PRIMARY}}}}</a>
          <a href="tel:{{{{PHONE_INTL}}}}" class="btn-phone btn-outline inline-flex items-center gap-1.5 border-2 border-white/30 text-white font-bold text-sm px-8 py-4 rounded-lg tracking-wide uppercase">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="flex-shrink-0"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg>
            <span>{{{{PHONE_DISPLAY}}}}</span>
          </a>
        </div>
      </div>
      <button class="hamburger lg:hidden flex flex-col justify-center items-center gap-[5px] w-10 h-10 relative z-[60]" aria-label="Menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </nav>

  <!-- Mobile menu -->
  <div class="mobile-menu fixed inset-0 z-[55] bg-dark flex flex-col items-center justify-center gap-5">
    <a href="/#om-os" class="mobile-nav-link text-white text-2xl font-display">{{{{SECTION_ABOUT}}}}</a>
    <a href="/#ydelser" class="mobile-nav-link text-white text-2xl font-display">{{{{SECTION_SERVICES}}}}</a>
    <a href="/{{{{SERVICE_1_SLUG}}}}" class="mobile-nav-link text-white/70 text-lg font-display">{{{{SERVICE_1_NAME}}}}</a>
    <a href="/{{{{SERVICE_2_SLUG}}}}" class="mobile-nav-link text-white/70 text-lg font-display">{{{{SERVICE_2_NAME}}}}</a>
    <a href="/{{{{SERVICE_3_SLUG}}}}" class="mobile-nav-link text-white/70 text-lg font-display">{{{{SERVICE_3_NAME}}}}</a>
    <a href="/{{{{SERVICE_4_SLUG}}}}" class="mobile-nav-link text-white/70 text-lg font-display">{{{{SERVICE_4_NAME}}}}</a>
    <a href="/{{{{SERVICE_5_SLUG}}}}" class="mobile-nav-link text-white/70 text-lg font-display">{{{{SERVICE_5_NAME}}}}</a>
    <a href="/#proces" class="mobile-nav-link text-white text-2xl font-display">{{{{NAV_PROCESS}}}}</a>
    <a href="/#galleri" class="mobile-nav-link text-white text-2xl font-display">{{{{SECTION_GALLERY}}}}</a>
    <a href="/#faq" class="mobile-nav-link text-white text-2xl font-display">{{{{NAV_FAQ}}}}</a>
    <a href="#" data-quote-trigger class="btn-primary mt-4 inline-block bg-brand text-white font-bold text-sm px-8 py-4 rounded-lg tracking-wide uppercase">{{{{CTA_PRIMARY}}}}</a>
  </div>

  <!-- HERO -->
  <section id="hero" class="relative min-h-[75vh] flex items-center justify-center grain overflow-hidden pt-32 pb-20 px-6 lg:px-8">
    <div class="absolute inset-0">
      <img src="/brand-assets/subpage-{n}.webp" alt="" aria-hidden="true" class="w-full h-full object-cover" fetchpriority="high" onerror="this.src='/brand-assets/hero.webp'">
      <div class="absolute inset-0 bg-gradient-to-b from-dark/70 via-dark/50 to-dark/80"></div>
    </div>
    <div class="relative z-10 max-w-4xl mx-auto text-center">
      <p class="text-brand font-medium text-sm tracking-[0.2em] uppercase mb-4">{{{{SERVICE_{n}_NAME}}}}</p>
      <h1 class="font-display text-white text-4xl sm:text-5xl lg:text-6xl xl:text-7xl leading-[1.1] mb-6" style="text-shadow: 0 2px 20px rgba(0,0,0,0.5)">{{{{SUBPAGE_{n}_HERO_HEADLINE}}}}</h1>
      <p class="text-white/80 text-lg md:text-xl leading-relaxed max-w-2xl mx-auto mb-10" style="text-shadow: 0 2px 12px rgba(0,0,0,0.6)">{{{{SUBPAGE_{n}_HERO_BODY}}}}</p>
      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <a href="#" data-quote-trigger class="btn-primary inline-block bg-brand text-white font-bold text-sm px-8 py-4 rounded-lg tracking-wide uppercase">{{{{CTA_PRIMARY}}}}</a>
        <a href="tel:{{{{PHONE_INTL}}}}" class="btn-outline border-2 border-white/30 text-white font-bold text-sm px-8 py-4 rounded-lg tracking-wide uppercase inline-block">Call {{{{PHONE_DISPLAY}}}}</a>
      </div>
      <p class="text-white/60 text-sm mt-8">{{{{SUBPAGE_AREA_FOOTNOTE}}}}</p>
    </div>
  </section>

  <!-- WHAT WE DO -->
  <section class="py-20 md:py-24 px-6 lg:px-8 bg-white">
    <div class="max-w-6xl mx-auto">
      <div class="text-center mb-16">
        <p class="text-brand font-medium text-sm tracking-[0.2em] uppercase mb-4">What we cover</p>
        <h2 class="font-display text-ink text-3xl md:text-4xl leading-[1.15]">{{{{SUBPAGE_{n}_SECTION_HEADLINE}}}}</h2>
      </div>
      <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <div class="bg-cream rounded-2xl p-8">
          <h3 class="font-display text-ink text-xl mb-3">{{{{SUBPAGE_{n}_DETAIL_1_TITLE}}}}</h3>
          <p class="text-muted leading-relaxed">{{{{SUBPAGE_{n}_DETAIL_1_BODY}}}}</p>
        </div>
        <div class="bg-cream rounded-2xl p-8">
          <h3 class="font-display text-ink text-xl mb-3">{{{{SUBPAGE_{n}_DETAIL_2_TITLE}}}}</h3>
          <p class="text-muted leading-relaxed">{{{{SUBPAGE_{n}_DETAIL_2_BODY}}}}</p>
        </div>
        <div class="bg-cream rounded-2xl p-8">
          <h3 class="font-display text-ink text-xl mb-3">{{{{SUBPAGE_{n}_DETAIL_3_TITLE}}}}</h3>
          <p class="text-muted leading-relaxed">{{{{SUBPAGE_{n}_DETAIL_3_BODY}}}}</p>
        </div>
        <div class="bg-cream rounded-2xl p-8">
          <h3 class="font-display text-ink text-xl mb-3">{{{{SUBPAGE_{n}_DETAIL_4_TITLE}}}}</h3>
          <p class="text-muted leading-relaxed">{{{{SUBPAGE_{n}_DETAIL_4_BODY}}}}</p>
        </div>
        <div class="bg-cream rounded-2xl p-8">
          <h3 class="font-display text-ink text-xl mb-3">{{{{SUBPAGE_{n}_DETAIL_5_TITLE}}}}</h3>
          <p class="text-muted leading-relaxed">{{{{SUBPAGE_{n}_DETAIL_5_BODY}}}}</p>
        </div>
        <div class="bg-cream rounded-2xl p-8">
          <h3 class="font-display text-ink text-xl mb-3">{{{{SUBPAGE_{n}_DETAIL_6_TITLE}}}}</h3>
          <p class="text-muted leading-relaxed">{{{{SUBPAGE_{n}_DETAIL_6_BODY}}}}</p>
        </div>
      </div>
    </div>
  </section>

  <!-- PROCESS -->
  <section class="py-20 md:py-24 px-6 lg:px-8 bg-cream">
    <div class="max-w-6xl mx-auto">
      <div class="text-center mb-16">
        <p class="text-brand font-medium text-sm tracking-[0.2em] uppercase mb-4">{{{{SECTION_PROCESS}}}}</p>
        <h2 class="font-display text-ink text-3xl md:text-4xl leading-[1.15]">{{{{SUBPAGE_PROCESS_HEADLINE}}}}</h2>
      </div>
      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-8">
        <div class="text-center">
          <div class="w-10 h-10 rounded-full bg-brand text-white font-bold flex items-center justify-center mx-auto mb-4 text-sm">1</div>
          <h3 class="font-display text-ink text-lg mb-2">{{{{PROCESS_1_TITLE}}}}</h3>
          <p class="text-muted text-sm leading-relaxed">{{{{PROCESS_1_DESC}}}}</p>
        </div>
        <div class="text-center">
          <div class="w-10 h-10 rounded-full bg-brand text-white font-bold flex items-center justify-center mx-auto mb-4 text-sm">2</div>
          <h3 class="font-display text-ink text-lg mb-2">{{{{PROCESS_2_TITLE}}}}</h3>
          <p class="text-muted text-sm leading-relaxed">{{{{PROCESS_2_DESC}}}}</p>
        </div>
        <div class="text-center">
          <div class="w-10 h-10 rounded-full bg-brand text-white font-bold flex items-center justify-center mx-auto mb-4 text-sm">3</div>
          <h3 class="font-display text-ink text-lg mb-2">{{{{PROCESS_3_TITLE}}}}</h3>
          <p class="text-muted text-sm leading-relaxed">{{{{PROCESS_3_DESC}}}}</p>
        </div>
        <div class="text-center">
          <div class="w-10 h-10 rounded-full bg-brand text-white font-bold flex items-center justify-center mx-auto mb-4 text-sm">4</div>
          <h3 class="font-display text-ink text-lg mb-2">{{{{PROCESS_4_TITLE}}}}</h3>
          <p class="text-muted text-sm leading-relaxed">{{{{PROCESS_4_DESC}}}}</p>
        </div>
      </div>
    </div>
  </section>

  <!-- PRICE -->
  <section class="py-20 md:py-24 px-6 lg:px-8 bg-white">
    <div class="max-w-4xl mx-auto">
      <div class="text-center mb-12">
        <p class="text-brand font-medium text-sm tracking-[0.2em] uppercase mb-4">Pricing</p>
        <h2 class="font-display text-ink text-3xl md:text-4xl leading-[1.15]">{{{{SUBPAGE_{n}_PRICE_HEADLINE}}}}</h2>
      </div>
      <div class="price-card rounded-2xl p-8 md:p-10">
        <p class="text-muted leading-relaxed mb-6">{{{{SUBPAGE_{n}_PRICE_INTRO}}}}</p>
        <h3 class="font-display text-ink text-xl mb-4">What affects the price</h3>
        <ul class="space-y-3 text-muted leading-relaxed mb-8">
          <li class="flex gap-3"><span class="text-brand flex-shrink-0">•</span> {{{{SUBPAGE_{n}_PRICE_FACTOR_1}}}}</li>
          <li class="flex gap-3"><span class="text-brand flex-shrink-0">•</span> {{{{SUBPAGE_{n}_PRICE_FACTOR_2}}}}</li>
          <li class="flex gap-3"><span class="text-brand flex-shrink-0">•</span> {{{{SUBPAGE_{n}_PRICE_FACTOR_3}}}}</li>
          <li class="flex gap-3"><span class="text-brand flex-shrink-0">•</span> {{{{SUBPAGE_{n}_PRICE_FACTOR_4}}}}</li>
          <li class="flex gap-3"><span class="text-brand flex-shrink-0">•</span> {{{{SUBPAGE_{n}_PRICE_FACTOR_5}}}}</li>
        </ul>
        <p class="text-muted leading-relaxed mb-8">{{{{SUBPAGE_{n}_PRICE_OUTRO}}}}</p>
        <a href="#" data-quote-trigger class="btn-primary inline-block bg-brand text-white font-bold text-sm px-8 py-4 rounded-lg tracking-wide uppercase">{{{{CTA_PRIMARY}}}}</a>
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="py-20 md:py-24 px-6 lg:px-8 bg-cream">
    <div class="max-w-3xl mx-auto">
      <div class="text-center mb-12">
        <p class="text-brand font-medium text-sm tracking-[0.2em] uppercase mb-4">{{{{NAV_FAQ}}}}</p>
        <h2 class="font-display text-ink text-3xl md:text-4xl leading-[1.15]">Common questions</h2>
      </div>
      <div class="bg-white rounded-2xl p-2 md:p-4">
        <div class="faq-item">
          <button class="faq-toggle w-full flex items-center justify-between px-6 py-5 text-left">
            <span class="font-medium text-ink text-lg pr-4">{{{{SUBPAGE_{n}_FAQ_1_Q}}}}</span>
            <svg class="faq-chevron w-5 h-5 text-muted flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer px-6"><p class="text-muted leading-relaxed pb-5">{{{{SUBPAGE_{n}_FAQ_1_A}}}}</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-toggle w-full flex items-center justify-between px-6 py-5 text-left">
            <span class="font-medium text-ink text-lg pr-4">{{{{SUBPAGE_{n}_FAQ_2_Q}}}}</span>
            <svg class="faq-chevron w-5 h-5 text-muted flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer px-6"><p class="text-muted leading-relaxed pb-5">{{{{SUBPAGE_{n}_FAQ_2_A}}}}</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-toggle w-full flex items-center justify-between px-6 py-5 text-left">
            <span class="font-medium text-ink text-lg pr-4">{{{{SUBPAGE_{n}_FAQ_3_Q}}}}</span>
            <svg class="faq-chevron w-5 h-5 text-muted flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer px-6"><p class="text-muted leading-relaxed pb-5">{{{{SUBPAGE_{n}_FAQ_3_A}}}}</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-toggle w-full flex items-center justify-between px-6 py-5 text-left">
            <span class="font-medium text-ink text-lg pr-4">{{{{SUBPAGE_{n}_FAQ_4_Q}}}}</span>
            <svg class="faq-chevron w-5 h-5 text-muted flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer px-6"><p class="text-muted leading-relaxed pb-5">{{{{SUBPAGE_{n}_FAQ_4_A}}}}</p></div>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="py-20 md:py-24 px-6 lg:px-8 bg-dark text-white">
    <div class="max-w-3xl mx-auto text-center">
      <h2 class="font-display text-3xl md:text-4xl leading-[1.15] mb-6">{{{{SUBPAGE_{n}_CTA_HEADLINE}}}}</h2>
      <p class="text-white/70 text-lg leading-relaxed mb-10">{{{{SUBPAGE_{n}_CTA_BODY}}}}</p>
      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <a href="tel:{{{{PHONE_INTL}}}}" class="btn-primary inline-flex items-center justify-center gap-2 bg-brand text-white font-bold text-sm px-8 py-4 rounded-lg tracking-wide uppercase">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"/></svg>
          Call {{{{PHONE_DISPLAY}}}}
        </a>
        <a href="#" data-quote-trigger class="btn-outline border-2 border-white/30 text-white font-bold text-sm px-8 py-4 rounded-lg tracking-wide uppercase inline-block">{{{{CTA_PRIMARY}}}}</a>
      </div>
    </div>
  </section>

  <!-- RELATED -->
  <section class="py-16 md:py-20 px-6 lg:px-8 bg-white">
    <div class="max-w-6xl mx-auto">
      <div class="text-center mb-12">
        <p class="text-brand font-medium text-sm tracking-[0.2em] uppercase mb-4">More services</p>
        <h2 class="font-display text-ink text-2xl md:text-3xl leading-[1.15]">We also handle</h2>
      </div>
      <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <a href="/{{{{SERVICE_{a}_SLUG}}}}" class="bg-cream rounded-2xl p-6 hover:shadow-lg transition-shadow">
          <h3 class="font-display text-ink text-lg mb-2">{{{{SERVICE_{a}_NAME}}}}</h3>
          <p class="text-muted text-sm leading-relaxed">{{{{SERVICE_{a}_BLURB}}}}</p>
        </a>
        <a href="/{{{{SERVICE_{b}_SLUG}}}}" class="bg-cream rounded-2xl p-6 hover:shadow-lg transition-shadow">
          <h3 class="font-display text-ink text-lg mb-2">{{{{SERVICE_{b}_NAME}}}}</h3>
          <p class="text-muted text-sm leading-relaxed">{{{{SERVICE_{b}_BLURB}}}}</p>
        </a>
        <a href="/{{{{SERVICE_{c}_SLUG}}}}" class="bg-cream rounded-2xl p-6 hover:shadow-lg transition-shadow">
          <h3 class="font-display text-ink text-lg mb-2">{{{{SERVICE_{c}_NAME}}}}</h3>
          <p class="text-muted text-sm leading-relaxed">{{{{SERVICE_{c}_BLURB}}}}</p>
        </a>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="bg-dark text-white/70 pt-20 pb-8 px-6">
    <div class="max-w-6xl mx-auto">
      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-12 mb-16">
        <div class="lg:col-span-1">
          <img src="/brand-assets/logo-280.webp" alt="{{{{LOGO_ALT}}}}" width="280" height="280" loading="lazy" class="w-auto mb-4" style="height: 140px; margin-top: -50px; margin-bottom: -40px;">
          <p class="text-sm leading-relaxed mb-6 mt-2">{{{{FOOTER_TAGLINE}}}}</p>
          <a href="{{{{INSTAGRAM_URL}}}}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 text-sm hover:text-brand transition-colors">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="5"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
            {{{{INSTAGRAM_HANDLE}}}}
          </a>
          <a href="{{{{FACEBOOK_URL}}}}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 text-sm hover:text-brand transition-colors mt-2">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
            {{{{BUSINESS_NAME}}}}
          </a>
        </div>
        <div>
          <p class="font-medium text-white text-sm uppercase tracking-wider mb-4">{{{{FOOTER_NAV_LABEL}}}}</p>
          <ul class="space-y-3 text-sm">
            <li><a href="/#om-os" class="hover:text-brand transition-colors">{{{{SECTION_ABOUT}}}}</a></li>
            <li><a href="/#ydelser" class="hover:text-brand transition-colors">{{{{SECTION_SERVICES}}}}</a></li>
            <li><a href="/#proces" class="hover:text-brand transition-colors">{{{{NAV_PROCESS}}}}</a></li>
            <li><a href="/#galleri" class="hover:text-brand transition-colors">{{{{SECTION_GALLERY}}}}</a></li>
            <li><a href="/#faq" class="hover:text-brand transition-colors">{{{{NAV_FAQ}}}}</a></li>
          </ul>
        </div>
        <div>
          <p class="font-medium text-white text-sm uppercase tracking-wider mb-4">{{{{SECTION_SERVICES}}}}</p>
          <ul class="space-y-3 text-sm">
            <li><a href="/{{{{SERVICE_1_SLUG}}}}" class="hover:text-brand transition-colors">{{{{SERVICE_1_NAME}}}}</a></li>
            <li><a href="/{{{{SERVICE_2_SLUG}}}}" class="hover:text-brand transition-colors">{{{{SERVICE_2_NAME}}}}</a></li>
            <li><a href="/{{{{SERVICE_3_SLUG}}}}" class="hover:text-brand transition-colors">{{{{SERVICE_3_NAME}}}}</a></li>
            <li><a href="/{{{{SERVICE_4_SLUG}}}}" class="hover:text-brand transition-colors">{{{{SERVICE_4_NAME}}}}</a></li>
            <li><a href="/{{{{SERVICE_5_SLUG}}}}" class="hover:text-brand transition-colors">{{{{SERVICE_5_NAME}}}}</a></li>
          </ul>
        </div>
        <div>
          <p class="font-medium text-white text-sm uppercase tracking-wider mb-4">{{{{FOOTER_CONTACT_LABEL}}}}</p>
          <ul class="space-y-3 text-sm">
            <li><a href="tel:{{{{PHONE_INTL}}}}" class="hover:text-brand transition-colors">{{{{PHONE_DISPLAY}}}}</a></li>
            <li><a href="mailto:{{{{EMAIL}}}}" class="hover:text-brand transition-colors">{{{{EMAIL}}}}</a></li>
            <li>{{{{STREET}}}}<br>{{{{POSTAL}}}} {{{{CITY_PRIMARY}}}}</li>
            <li>{{{{TRUST_2_TITLE}}}}: {{{{LICENSE_ID}}}}</li>
            <li class="pt-2 border-t border-white/10 mt-3">{{{{HOURS_DISPLAY}}}}</li>
          </ul>
        </div>
      </div>
      <div class="border-t border-white/10 pt-8 pb-6 flex flex-wrap justify-center gap-x-6 gap-y-2 text-xs">
        <a href="/{{{{LEGAL_PRIVACY_SLUG}}}}" class="text-white/60 hover:text-brand transition-colors">{{{{LEGAL_PRIVACY_LABEL}}}}</a>
        <a href="/{{{{LEGAL_TERMS_SLUG}}}}" class="text-white/60 hover:text-brand transition-colors">{{{{LEGAL_TERMS_LABEL}}}}</a>
        <a href="/{{{{LEGAL_COOKIE_SLUG}}}}" class="text-white/60 hover:text-brand transition-colors">{{{{LEGAL_COOKIE_LABEL}}}}</a>
      </div>
      <div class="flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-white/40">
        <p>&copy; {{{{YEAR}}}} {{{{BUSINESS_NAME}}}}. {{{{COPYRIGHT_TAIL}}}}</p>
        <p>{{{{CREDIT_LABEL}}}} <a href="https://loopiai.com" target="_blank" rel="noopener noreferrer" class="text-brand/60 hover:text-brand transition-colors">Loopi AI</a></p>
      </div>
    </div>
  </footer>

  <!-- FAQ toggle script (same behavior as homepage) -->
  <script>
    document.querySelectorAll('.faq-toggle').forEach(toggle => {{
      toggle.addEventListener('click', () => {{
        const item = toggle.parentElement;
        const answer = item.querySelector('.faq-answer');
        const chevron = item.querySelector('.faq-chevron');
        const isOpen = answer.classList.contains('open');
        document.querySelectorAll('.faq-answer').forEach(a => a.classList.remove('open'));
        document.querySelectorAll('.faq-chevron').forEach(c => c.classList.remove('rotated'));
        item.classList.toggle('open', !isOpen);
        if (!isOpen) {{ answer.classList.add('open'); chevron.classList.add('rotated'); }}
      }});
    }});

    // Mobile menu
    const hamburger = document.querySelector('.hamburger');
    const mobileMenu = document.querySelector('.mobile-menu');
    hamburger?.addEventListener('click', () => {{
      hamburger.classList.toggle('active');
      mobileMenu.classList.toggle('open');
      document.body.style.overflow = mobileMenu.classList.contains('open') ? 'hidden' : '';
    }});
    document.querySelectorAll('.mobile-nav-link').forEach(l => l.addEventListener('click', () => {{
      hamburger.classList.remove('active');
      mobileMenu.classList.remove('open');
      document.body.style.overflow = '';
    }}));

    // Nav scroll state
    const nav = document.querySelector('.nav-bar');
    const toggleNav = () => nav?.classList.toggle('scrolled', window.scrollY > 0);
    window.addEventListener('scroll', toggleNav, {{ passive: true }});
    toggleNav();
  </script>

</body>
</html>
"""


for name, n in SUBPAGES.items():
    (ROOT / name).write_text(page(n), encoding='utf-8')
    print(f"wrote {name} (SERVICE_{n})")
print("done.")
