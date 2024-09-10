import { defineConfig, squooshImageService } from 'astro/config';

import preact from "@astrojs/preact";

// https://astro.build/config
export default defineConfig({
  image: {
    service: squooshImageService()
  },
  // https://docs.astro.build/en/guides/deploy/github/#using-github-pages-with-a-custom-domain
  site: 'https://hcc.rschubkegel.xyz',
  integrations: [preact()]
});