import type { InferEntrySchema } from 'astro:content';
import { DateTime } from 'luxon';

export const SYMBOLS: Record<InferEntrySchema<'weekly-resources'>['resources'][number]['type'], string> = {
  'article': '📖',
  'assignment': '📝',
  'slides': '🎞️',
  'video': '📽️',
};

export const capitalizeString = (str: string) => str.charAt(0).toUpperCase() + str.slice(1);

/** Takes a starting date in ISO format (`YYYY-MM-DD`) and returns a formatted string. */
export const formatWeekString = (isoString: string, { duration }: { duration?: number } = {}) => {
  const start = DateTime.fromISO(isoString, { zone: 'America/Los_Angeles' });
  duration = duration ?? (1000 * 60 * 60 * 24 * 6);
  const end = DateTime.fromMillis(start.toMillis() + duration);
  const startString = start.toFormat('MMM dd');
  const monthDiffers = start.month !== end.month;
  const endString = end.toFormat(monthDiffers ? 'MMM dd' : 'dd');
  return `${startString}–${endString}`;
};

/** Unslugifies a string */
export const unslugify = (str: string) => str.split('-').map(x => x.charAt(0).toUpperCase() + x.slice(1)).join(' ');

/** Checks if a string is an external link */
export const isHrefExternal = (href: string) => /^https?:\/\//.test(href);