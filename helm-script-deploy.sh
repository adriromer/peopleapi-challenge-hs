#!/usr/bin/env bash
set +x
f_output () 
{
  echo "$(date) : ${@}"
}
usage ()
{
  echo "USAGE : "
  echo "    ${0}  -n 'namespace'"
  exit 3
}
read_parametros ()
{
  if [ ${#} -lt 1 ] ; then
    usage
    return 3
  fi
    case ${1} in
      -n)
        shift
        if ! [ -z ${1} ] ; then
          namespace="${@}"
        else
          usage
        fi
      ;;
      *)
        usage
      ;;
    esac
}
create_helm () 
{
  if [ $(kubectl get ns | grep "^${namespace} "|wc -l) -eq 0  ] ; then
    f_output "NameSpace ${namespace} not found Creating NameSpace for peopleapi-challenge-hs Helm Chart"
    f_output "create namespace ${namespace}"
    f_output "$(kubectl create ns ${namespace})"
  fi
  if [ -n "${namespace}" ] ; then
    f_output "Installing Helm Chart peopleapi-challenge-hs with Values form helm/value.yaml in ${namespace} name space"
    cd helm
    helm install peopleapi-challenge-hs . -n ${namespace}
    cd -
  fi
}
main ()
{
  read_parametros ${@}
  create_helm
}
main ${@}
