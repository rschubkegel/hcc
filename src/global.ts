import type { InferEntrySchema } from 'astro:content';

export const SYMBOLS: Record<InferEntrySchema<'weekly-resources'>['resources'][number]['type'], string> = {
  'article': '📖',
  'assignment': '📝',
  'slides': '🎞️',
  'video': '📽️',
};

export const capitalizeString = (str: string) => str.charAt(0).toUpperCase() + str.slice(1);

/** Takes a starting date in ISO format (`YYYY-MM-DD`) and returns a formatted string. */
export const formatWeekString = (isoString: string) => {
  const offsetMillis = 1000 * 60 * 60 * 24 * 6;
  const start = new Date(isoString);
  const end = new Date(start.getTime() + offsetMillis);
  const startString = start.toLocaleString('en-US', { month: 'short', day: '2-digit' });
  const monthDiffers = start.getMonth() !== end.getMonth();
  const endString = monthDiffers
    ? end.toLocaleString('en-US', { month: 'short', day: '2-digit' })
    : end.toLocaleString('en-US', { day: '2-digit' });
  return `${startString}–${endString}`;
};