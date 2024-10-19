import { z, defineCollection } from 'astro:content';

const basicResourceSchema = z.object({
  /** Title of the resource */
  title: z.string(),
  /** URL of the resource */
  href: z.string().optional(),
  /** Type of resource */
  type: z.enum(['slides', 'video', 'article', 'assignment']),
  /** Time estimate (in minutes); used to estimate student effort */
  time: z.number(),
});

const resourcesSchema = z.array(
  z.objectUtil.mergeShapes(
    basicResourceSchema,
    z.object({
      /** Description of the resource */
      description: z.string().optional(),
    }),
  ),
);

const slidesSchema = z.object({
  /** Date of the class that the slides are created for. */
  date: z.date(),
  /** Title of the slideshow. */
  title: z.string(),
});

const weeklyResourcesSchema = z.object({
  /** List of topics covered this week */
  topics: z.array(z.string()),
  /** List of resources for this week */
  resources: z.array(basicResourceSchema),
});

export const collections = {
  'resources': defineCollection({
    type: 'data',
    schema: resourcesSchema,
  }),
  'slides': defineCollection({
    type: 'content',
    schema: slidesSchema,
  }),
  'weekly-resources': defineCollection({
    type: 'data',
    schema: weeklyResourcesSchema,
  }),
};