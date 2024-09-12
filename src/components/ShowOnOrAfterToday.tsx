/**
 * Shows child content if today is after the specified date.
 */

import type { JSX } from 'preact/jsx-runtime';
import { assignedBeforeNow } from 'src/global';

type TProps = {
  children: JSX.ElementChildrenAttribute;
  /** ISO 8601 date string */
  date: string;
}

export default (props: TProps) => {
  const afterToday = assignedBeforeNow(props.date);
  return afterToday ? props.children : null;
}