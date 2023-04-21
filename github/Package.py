import github
import github.NamedUser
import github.PaginatedList


class Common(github.GithubObject.CompletableGithubObject):

    @property
    def id(self):
        """
        :type: int
        """
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def name(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._url.value

    def _initAttributes(self):
        self._id = github.GithubObject.NotSet
        self._name = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._updated_at = github.GithubObject.NotSet
        self._html_url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])


class PackageMetaData(github.GithubObject.CompletableGithubObject):
    def _initAttributes(self):
        self._package_type = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "package_type" in attributes:  # pragma no branch
            self._package_type = self._makeStringAttribute(attributes["package_type"])


class PackageVersion(Common):
    def _initAttributes(self):
        super(PackageVersion, self)._initAttributes()
        self._package_html_url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        super(PackageVersion, self)._useAttributes(attributes)
        if "package_html_url" in attributes:  # pragma no branch
            self._package_html_url = self._makeStringAttribute(attributes["package_html_url"])
        if "metadata" in attributes:
            self._metadata = self._makeClassAttribute(
                PackageMetaData, attributes["metadata"]
            )


class Package(Common):

    def get_versions(self):
        """
        :calls: `GET /repos/{owner}/{repo}/assignees <https://docs.github.com/en/rest/reference/issues#assignees>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Package.PackageVersion`
        """
        return github.PaginatedList.PaginatedList(
            PackageVersion, self._requester, f"{self.url}/versions", None
        )

    def _initAttributes(self):
        super(Package, self)._initAttributes()
        self._package_type = github.GithubObject.NotSet
        self._owner = github.GithubObject.NotSet
        self._version_count = github.GithubObject.NotSet
        self._visibility = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        super(Package, self)._useAttributes(attributes)
        if "package_type" in attributes:  # pragma no branch
            self._package_type = self._makeStringAttribute(attributes["package_type"])
        if "owner" in attributes:  # pragma no branch
            self._owner = self._makeClassAttribute(
                github.NamedUser.NamedUser, attributes["owner"]
            )
        if "version_count" in attributes:  # pragma no branch
            self._version_count = self._makeIntAttribute(
                attributes["version_count"]
            )
        if "visibility" in attributes:  # pragma no branch
            self._visibility = self._makeStringAttribute(attributes["visibility"])
        # if "allow_rebase_merge" in attributes:  # pragma no branch
        #     self._allow_rebase_merge = self._makeBoolAttribute(
        #         attributes["allow_rebase_merge"]
        #     )
        # if "allow_squash_merge" in attributes:  # pragma no branch
        #     self._allow_squash_merge = self._makeBoolAttribute(
        #         attributes["allow_squash_merge"]
        #     )
        # if "archived" in attributes:  # pragma no branch
        #     self._archived = self._makeBoolAttribute(attributes["archived"])
        # if "archive_url" in attributes:  # pragma no branch
        #     self._archive_url = self._makeStringAttribute(attributes["archive_url"])
        # if "assignees_url" in attributes:  # pragma no branch
        #     self._assignees_url = self._makeStringAttribute(attributes["assignees_url"])
        # if "blobs_url" in attributes:  # pragma no branch
        #     self._blobs_url = self._makeStringAttribute(attributes["blobs_url"])
        # if "branches_url" in attributes:  # pragma no branch
        #     self._branches_url = self._makeStringAttribute(attributes["branches_url"])
        # if "clone_url" in attributes:  # pragma no branch
        #     self._clone_url = self._makeStringAttribute(attributes["clone_url"])
        # if "collaborators_url" in attributes:  # pragma no branch
        #     self._collaborators_url = self._makeStringAttribute(
        #         attributes["collaborators_url"]
        #     )
        # if "comments_url" in attributes:  # pragma no branch
        #     self._comments_url = self._makeStringAttribute(attributes["comments_url"])
        # if "commits_url" in attributes:  # pragma no branch
        #     self._commits_url = self._makeStringAttribute(attributes["commits_url"])
        # if "compare_url" in attributes:  # pragma no branch
        #     self._compare_url = self._makeStringAttribute(attributes["compare_url"])
        # if "contents_url" in attributes:  # pragma no branch
        #     self._contents_url = self._makeStringAttribute(attributes["contents_url"])
        # if "contributors_url" in attributes:  # pragma no branch
        #     self._contributors_url = self._makeStringAttribute(
        #         attributes["contributors_url"]
        #     )
        #
        # if "default_branch" in attributes:  # pragma no branch
        #     self._default_branch = self._makeStringAttribute(
        #         attributes["default_branch"]
        #     )
        # if "delete_branch_on_merge" in attributes:  # pragma no branch
        #     self._delete_branch_on_merge = self._makeBoolAttribute(
        #         attributes["delete_branch_on_merge"]
        #     )
        # if "deployments_url" in attributes:  # pragma no branch
        #     self._deployments_url = self._makeStringAttribute(
        #         attributes["deployments_url"]
        #     )
        # if "description" in attributes:  # pragma no branch
        #     self._description = self._makeStringAttribute(attributes["description"])
        # if "downloads_url" in attributes:  # pragma no branch
        #     self._downloads_url = self._makeStringAttribute(attributes["downloads_url"])
        # if "events_url" in attributes:  # pragma no branch
        #     self._events_url = self._makeStringAttribute(attributes["events_url"])
        # if "fork" in attributes:  # pragma no branch
        #     self._fork = self._makeBoolAttribute(attributes["fork"])
        # if "forks" in attributes:  # pragma no branch
        #     self._forks = self._makeIntAttribute(attributes["forks"])
        # if "forks_count" in attributes:  # pragma no branch
        #     self._forks_count = self._makeIntAttribute(attributes["forks_count"])
        # if "forks_url" in attributes:  # pragma no branch
        #     self._forks_url = self._makeStringAttribute(attributes["forks_url"])
        # if "full_name" in attributes:  # pragma no branch
        #     self._full_name = self._makeStringAttribute(attributes["full_name"])
        # if "git_commits_url" in attributes:  # pragma no branch
        #     self._git_commits_url = self._makeStringAttribute(
        #         attributes["git_commits_url"]
        #     )
        # if "git_refs_url" in attributes:  # pragma no branch
        #     self._git_refs_url = self._makeStringAttribute(attributes["git_refs_url"])
        # if "git_tags_url" in attributes:  # pragma no branch
        #     self._git_tags_url = self._makeStringAttribute(attributes["git_tags_url"])
        # if "git_url" in attributes:  # pragma no branch
        #     self._git_url = self._makeStringAttribute(attributes["git_url"])
        # if "has_downloads" in attributes:  # pragma no branch
        #     self._has_downloads = self._makeBoolAttribute(attributes["has_downloads"])
        # if "has_issues" in attributes:  # pragma no branch
        #     self._has_issues = self._makeBoolAttribute(attributes["has_issues"])
        # if "has_pages" in attributes:  # pragma no branch
        #     self._has_pages = self._makeBoolAttribute(attributes["has_pages"])
        # if "has_projects" in attributes:  # pragma no branch
        #     self._has_projects = self._makeBoolAttribute(attributes["has_projects"])
        # if "has_wiki" in attributes:  # pragma no branch
        #     self._has_wiki = self._makeBoolAttribute(attributes["has_wiki"])
        # if "homepage" in attributes:  # pragma no branch
        #     self._homepage = self._makeStringAttribute(attributes["homepage"])
        # if "hooks_url" in attributes:  # pragma no branch
        #     self._hooks_url = self._makeStringAttribute(attributes["hooks_url"])
        #
        #
        # if "is_template" in attributes:  # pragma no branch
        #     self._is_template = self._makeBoolAttribute(attributes["is_template"])
        # if "issue_comment_url" in attributes:  # pragma no branch
        #     self._issue_comment_url = self._makeStringAttribute(
        #         attributes["issue_comment_url"]
        #     )
        # if "issue_events_url" in attributes:  # pragma no branch
        #     self._issue_events_url = self._makeStringAttribute(
        #         attributes["issue_events_url"]
        #     )
        # if "issues_url" in attributes:  # pragma no branch
        #     self._issues_url = self._makeStringAttribute(attributes["issues_url"])
        # if "keys_url" in attributes:  # pragma no branch
        #     self._keys_url = self._makeStringAttribute(attributes["keys_url"])
        # if "labels_url" in attributes:  # pragma no branch
        #     self._labels_url = self._makeStringAttribute(attributes["labels_url"])
        # if "language" in attributes:  # pragma no branch
        #     self._language = self._makeStringAttribute(attributes["language"])
        # if "languages_url" in attributes:  # pragma no branch
        #     self._languages_url = self._makeStringAttribute(attributes["languages_url"])
        # if "master_branch" in attributes:  # pragma no branch
        #     self._master_branch = self._makeStringAttribute(attributes["master_branch"])
        # if "merges_url" in attributes:  # pragma no branch
        #     self._merges_url = self._makeStringAttribute(attributes["merges_url"])
        # if "milestones_url" in attributes:  # pragma no branch
        #     self._milestones_url = self._makeStringAttribute(
        #         attributes["milestones_url"]
        #     )
        # if "mirror_url" in attributes:  # pragma no branch
        #     self._mirror_url = self._makeStringAttribute(attributes["mirror_url"])
        #
        # if "network_count" in attributes:  # pragma no branch
        #     self._network_count = self._makeIntAttribute(attributes["network_count"])
        # if "notifications_url" in attributes:  # pragma no branch
        #     self._notifications_url = self._makeStringAttribute(
        #         attributes["notifications_url"]
        #     )
        # if "open_issues" in attributes:  # pragma no branch
        #     self._open_issues = self._makeIntAttribute(attributes["open_issues"])
        # if "open_issues_count" in attributes:  # pragma no branch
        #     self._open_issues_count = self._makeIntAttribute(
        #         attributes["open_issues_count"]
        #     )
        # if "organization" in attributes:  # pragma no branch
        #     self._organization = self._makeClassAttribute(
        #         github.Organization.Organization, attributes["organization"]
        #     )
        # if "parent" in attributes:  # pragma no branch
        #     self._parent = self._makeClassAttribute(Package, attributes["parent"])
        # if "permissions" in attributes:  # pragma no branch
        #     self._permissions = self._makeClassAttribute(
        #         github.Permissions.Permissions, attributes["permissions"]
        #     )
        # if "private" in attributes:  # pragma no branch
        #     self._private = self._makeBoolAttribute(attributes["private"])
        # if "pulls_url" in attributes:  # pragma no branch
        #     self._pulls_url = self._makeStringAttribute(attributes["pulls_url"])
        # if "pushed_at" in attributes:  # pragma no branch
        #     self._pushed_at = self._makeDatetimeAttribute(attributes["pushed_at"])
        # if "releases_url" in attributes:  # pragma no branch
        #     self._releases_url = self._makeStringAttribute(attributes["releases_url"])
        # if "size" in attributes:  # pragma no branch
        #     self._size = self._makeIntAttribute(attributes["size"])
        # if "source" in attributes:  # pragma no branch
        #     self._source = self._makeClassAttribute(Package, attributes["source"])
        # if "ssh_url" in attributes:  # pragma no branch
        #     self._ssh_url = self._makeStringAttribute(attributes["ssh_url"])
        # if "stargazers_count" in attributes:  # pragma no branch
        #     self._stargazers_count = self._makeIntAttribute(
        #         attributes["stargazers_count"]
        #     )
        # if "stargazers_url" in attributes:  # pragma no branch
        #     self._stargazers_url = self._makeStringAttribute(
        #         attributes["stargazers_url"]
        #     )
        # if "statuses_url" in attributes:  # pragma no branch
        #     self._statuses_url = self._makeStringAttribute(attributes["statuses_url"])
        # if "subscribers_url" in attributes:  # pragma no branch
        #     self._subscribers_url = self._makeStringAttribute(
        #         attributes["subscribers_url"]
        #     )
        # if "subscribers_count" in attributes:  # pragma no branch
        #     self._subscribers_count = self._makeIntAttribute(
        #         attributes["subscribers_count"]
        #     )
        # if "subscription_url" in attributes:  # pragma no branch
        #     self._subscription_url = self._makeStringAttribute(
        #         attributes["subscription_url"]
        #     )
        # if "svn_url" in attributes:  # pragma no branch
        #     self._svn_url = self._makeStringAttribute(attributes["svn_url"])
        # if "tags_url" in attributes:  # pragma no branch
        #     self._tags_url = self._makeStringAttribute(attributes["tags_url"])
        # if "teams_url" in attributes:  # pragma no branch
        #     self._teams_url = self._makeStringAttribute(attributes["teams_url"])
        # if "trees_url" in attributes:  # pragma no branch
        #     self._trees_url = self._makeStringAttribute(attributes["trees_url"])
        # if "topics" in attributes:  # pragma no branch
        #     self._topics = self._makeListOfStringsAttribute(attributes["topics"])
        #
        #
        # if "watchers" in attributes:  # pragma no branch
        #     self._watchers = self._makeIntAttribute(attributes["watchers"])
        # if "watchers_count" in attributes:  # pragma no branch
        #     self._watchers_count = self._makeIntAttribute(attributes["watchers_count"])
