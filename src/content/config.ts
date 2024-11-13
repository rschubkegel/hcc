import { z, defineCollection } from 'astro:content';

const assignmentsSchema = z.object({
  /** Date the assignment is due. If `undefined`, assignment does not need to be turned in. */
  endDate: z.date().optional(),
  /** Name of the assignment (used in h1). */
  name: z.string(),
  /** Date the assignment begins. */
  startDate: z.date(),
  /** Assignment title (used in webpage title). */
  title: z.string().optional(),
});

const basicResourceSchema = z.object({
  /** Title of the resource */
  title: z.string(),
  /** URL of the resource */
  href: z.string().optional(),
  /** Type of resource */
  type: z.enum(['slides', 'video', 'article', 'assignment', 'game']),
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
  'assignments': defineCollection({
    type: 'content',
    schema: assignmentsSchema,
  }),
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