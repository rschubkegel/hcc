/**
 * Shows child content once authenticated via password.
 *
 * NOTE: this is *not secure* because it just checks input against a hardcoded password.
 */

import { useCallback, useEffect, useRef, useState } from 'preact/compat';
import type { JSX } from 'preact/jsx-runtime';
import { GATEKEEPER_PASSWORD } from 'src/global';

type TProps = {
  children: JSX.ElementChildrenAttribute;
}

type TFormData = {
  password: string;
}

type TOnSubmit = (data: TFormData) => void;

const Form = ({ onSubmit }: { onSubmit: TOnSubmit }) => {
  const focusRef = useRef<HTMLInputElement>(null);
  const [password, setPassword] = useState('');
  const _onSubmit = useCallback<JSX.SubmitEventHandler<HTMLFormElement>>(event => {
    event.preventDefault();
    onSubmit({ password });
  }, [onSubmit, password]);
  const onInput = useCallback<JSX.GenericEventHandler<HTMLInputElement>>(event => {
    if (event.target instanceof HTMLInputElement) {
      setPassword(event.target.value);
      if (event instanceof KeyboardEvent && event.key === 'Enter') {
        onSubmit({ password });
      }
    }
  }, [setPassword]);
  const onChange = useCallback<JSX.GenericEventHandler<HTMLInputElement>>(event => {
    if (event.target instanceof HTMLInputElement) {
      setPassword(event.target.value);
    }
  }, [setPassword]);
  useEffect(() => {
    focusRef.current?.focus();
    setPassword(focusRef.current?.value || '');
  }, []);
  return (
    <form action="" onSubmitCapture={_onSubmit}>
      <div style="display: flex; gap: 1rem;">
        <input ref={focusRef} type="password" name="password" placeholder="Password" value={password} onInput={onInput} onChange={onChange} style="flex-grow: 1" />
        <input type="submit" value="Submit" />
      </div>
    </form>
  );
}

export default (props: TProps) => {
  const [admitted, setAdmitted] = useState(false);
  const onSubmit = useCallback<TOnSubmit>((data: TFormData) => {
    if (data.password === GATEKEEPER_PASSWORD) {
      setAdmitted(true);
    } else {
      alert('Incorrect password');
    }
  }, [setAdmitted]);
  return admitted ? props.children : <Form onSubmit={onSubmit} />
};